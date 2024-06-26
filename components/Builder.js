import React, { Component } from "react";
import Level, { Cell, TOKEN } from "./level";
import InputHandler from "../utils/inputHandler";
import LevelConfig from "../utils/levelConfig";
import solver from "../utils/workerManager";
import LibraryModal from "./LibraryModal";

if (typeof window !== "undefined") window.solver = solver;

function cloneDeep(obj) {
  return JSON.parse(JSON.stringify(obj));
}

function encodedState(definition) {
  return btoa(JSON.stringify(definition));
}

function decodedState(code) {
  if (!code?.length) return null;
  return JSON.parse(atob(code));
}

// thank you, chatgpt
function copyText(value) {
  // Use the Clipboard API if available
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard
      .writeText(value)
      .then(() => {
        alert("Level code copied to clipboard");
      })
      .catch((err) => {
        console.error("Failed to copy text: ", err);
      });
  } else {
    // Fallback for browsers that do not support the Clipboard API
    const textArea = document.createElement("textarea");
    textArea.value = value;
    document.body.appendChild(textArea);
    textArea.select();
    textArea.setSelectionRange(0, 99999); // For mobile devices
    document.execCommand("copy");
    document.body.removeChild(textArea);
    alert("Level code copied to clipboard");
  }
}

const LEGAL_TOKEN_PAIRS = [
  [TOKEN.COLLAPSE, TOKEN.COIN],
  [TOKEN.COLLAPSE, TOKEN.BARRIER],
  [TOKEN.FINISH1, TOKEN.COIN],
  [TOKEN.FINISH1, TOKEN.BARRIER],
  [TOKEN.FINISH1, TOKEN.PLAYER1],
  [TOKEN.DEATH, TOKEN.BARRIER],
];

function makeBlankDefinition(rows, cols) {
  const definition = [];
  for (let i = 0; i < rows; ++i) {
    const row = [];
    for (let j = 0; j < cols; ++j) {
      row.push([]);
    }
    definition.push(row);
  }
  return definition;
}

const { puzzles, groups } = require("./levels.json");
const defaultLevels = puzzles.map(
  ({ name, definition, groups, description }, index) =>
    new LevelConfig(index, name, definition, groups, description)
);

export function TokenButton({ type, onClick, active }) {
  const BASE_CLASS = "builder__tools__token-btn";
  const ACTIVE = BASE_CLASS + "--active";
  return (
    <div
      tabIndex={-1}
      onClick={onClick}
      className={BASE_CLASS + " " + (active ? ACTIVE : "")}
    >
      <Cell def={type ? [type] : []} size={30} />
    </div>
  );
}
export default class Builder extends Component {
  constructor(props) {
    super(props);

    this.inputHandler = new InputHandler();

    const defaultRows = 10,
      defaultCols = 10;

    this.analysisRequests = [];

    this.state = {
      rows: defaultRows,
      cols: defaultCols,
      definition: makeBlankDefinition(defaultRows, defaultCols),
      activeToken: TOKEN.WALL,
      version: 0,
      history: [],
      analysis: null,
      analyzing: false,
      libraryOpen: false,
      solverOn: true,
    };

    this.levelRef = React.createRef();
  }

  load(level) {
    this.clear(); // this resets the solver, etc.
    this.applyStateChange(level.definition);
  }

  copyDefinition() {
    copyText(JSON.stringify(this.state.definition));
  }

  toggleSolver() {
    this.clearAnalysis();
    const solverOn = !this.state.solverOn;
    this.setState({
      solverOn,
    });
    if (solverOn) {
      // This a bit hacky, but we need the current analysis
      // to reflect the live state of the board, not the initial definition.
      this.levelRef.current?.onchange();
    } 
  }

  promptDefinition() {
    const data = prompt(
      "Please enter the JSON definition of the level, in the same format that you'd get it e.g. from the COPY button."
    );

    try {
      const definition = JSON.parse(data);
      this.load({ definition });
    } catch (e) {
      console.error(e);
      alert("That didn't work, sorry: " + e.toString());
    }
  }

  componentDidMount() {
    if (typeof window === "undefined") {
      return;
    }
    // TODO: load state from URL (also update URL with state)
    const hash = window.location.hash?.slice(1);
    const state = decodedState(hash);
    if (state) {
      this.load({
        definition: state.definition,
      });
    }
  }

  clickHandler(props) {
    this.updateTokenAtPosition(props.row, props.col);
  }

  changeHandler(props) {
    this.updateAnalysis(props.board, props.deathByes);
  }

  updateTokenAtPosition(row, col) {
    const cur = this.state.definition[row]?.[col]?.slice();
    const cell = [];
    if (!cell) {
      console.log("Out of bounds access: ", row, col);
    }

    if (this.state.activeToken === TOKEN.EMPTY) {
      // Clear cell
    } else if (cur.length === 1 && cur[0] === this.state.activeToken) {
      // Clear cell
    } else if (!cur.length) {
      // Empty cell is filled with the active token
      cell.push(this.state.activeToken);
    } else if (
      cur.length === 1 &&
      LEGAL_TOKEN_PAIRS.find(
        ([a, b]) => a === cur[0] && b === this.state.activeToken
      )
    ) {
      // Cell is not empty, but we can 'stack' the selected token on top of it.
      cell.push(cur[0]);
      cell.push(this.state.activeToken);
    } else {
      cell.push(this.state.activeToken);
    }

    const newDefinition = cloneDeep(this.state.definition);
    newDefinition[row][col] = cell;
    this.applyStateChange(newDefinition);
  }

  clearAnalysis() {
    window.solver.refresh();
    this.setState({
      analysis: null,
      analyzing: false,
    });
  }

  clear() {
    window.location.hash = "";
    this.clearAnalysis();
    this.applyStateChange(
      makeBlankDefinition(this.state.rows, this.state.cols)
    );
  }

  applyStateChange(definition) {
    this.state.history.push(this.state.definition);
    this.setState({
      definition,
      version: this.state.version + 1,
      rows: definition.length,
      cols: definition[0].length,
    });
    // Update URL
    window.location.hash = encodedState({ definition });
  }

  updateAnalysis(definition, deathByes) {
    const pos = this.analysisRequests.length;
    console.log("requesting solve of def: ", definition);
    this.setState({ analyzing: true });
    this.analysisRequests.push(
      window.solver.solve(definition, deathByes).then((result) => {
        console.log("Got result!", result);
        if (this.analysisRequests.length !== pos + 1) {
          // Another request has been made since we initiated this request; abort.
          return;
        }
        this.setState({ analysis: result, analyzing: false });
      })
    );
  }

  processDimRaw(value) {
    value = [...value].filter((n) => "0123456789".includes(n)).join("");
    if (!value.length) return;
    let num = parseInt(value);
    if (num < 1) num = 1;
    if (num > 30) num = 30;
    return num;
  }

  setRows(value) {
    const num = this.processDimRaw(value);
    if (!num) return;

    const newDefinition = makeBlankDefinition(num, this.state.cols);
    for (let i = 0; i < num && i < this.state.rows; ++i) {
      for (let j = 0; j < this.state.cols; ++j) {
        newDefinition[i][j] = this.state.definition[i][j].slice();
      }
    }

    this.setState({ rows: num });
    this.applyStateChange(newDefinition);
  }

  setCols(value) {
    const num = this.processDimRaw(value);
    if (!num) return;

    const newDefinition = makeBlankDefinition(this.state.rows, num);
    for (let i = 0; i < this.state.rows; ++i) {
      for (let j = 0; j < num && j < this.state.cols; ++j) {
        newDefinition[i][j] = this.state.definition[i][j].slice();
      }
    }

    this.setState({ cols: num });
    this.applyStateChange(newDefinition);
  }

  render() {
    return (
      <div className={"builder-wrap"}>
        <h1 className={"game-title"}>Create Your Own Level</h1>
        <p>
          Tip: You can share this URL. Send us{" "}
          <a className="email" href="mailto:jacob.brazeal@gmail.com">
            an email
          </a>{" "}
          with a link to your puzzle. We might feature it in the future and
          credit you!
        </p>

        {/* TODO: Allow entering level + description */}

        <div className="builder">
          <div className="builder__main-pane">
            <Level
              definition={this.state.definition}
              inputHandler={this.inputHandler}
              key={this.state.version}
              onclick={this.clickHandler.bind(this)}
              onchange={this.changeHandler.bind(this)}
              ref={this.levelRef}
            />
          </div>
          <div className="builder__tools-pane">
            <div className="builder__tools__token-picker">
              {Object.values(TOKEN).map((token) => (
                <TokenButton
                  key={token}
                  active={token === this.state.activeToken}
                  type={token}
                  onClick={() => {
                    this.setState({
                      activeToken: token,
                    });
                  }}
                />
              ))}
            </div>
          </div>
          <div className="builder__tools-pane">
            <div className="builder__tools__dims">
              <input
                defaultValue={this.state.rows}
                key={"r" + this.state.rows}
                onChange={(e) => this.setRows(e.target.value)}
                className="builder__tools__dim"
              />
              &#10005;
              <input
                defaultValue={this.state.cols}
                key={"c" + this.state.cols}
                onChange={(e) => this.setCols(e.target.value)}
                className="builder__tools__dim"
              />
            </div>
            <div>
              <button className={"tool-btn"} onClick={() => this.clear()}>
                Clear
              </button>
            </div>
            <div>
              <button
                className={"tool-btn tool-btn--launch-library"}
                onClick={() => this.setState({ libraryOpen: true })}
              >
                Library
              </button>
            </div>
            <div>
              <button
                className={"tool-btn"}
                onClick={() => this.copyDefinition()}
              >
                Copy
              </button>
            </div>
            <div>
              <button
                className={"tool-btn"}
                onClick={() => this.promptDefinition()}
              >
                Load
              </button>
            </div>
            <div>
              <button
                className={"tool-btn"}
                onClick={() => this.toggleSolver()}
              >
                {this.state.solverOn ? "Manual" : "Help"}
              </button>
            </div>
            {this.state.solverOn &&
              (this.state.analysis || this.state.analyzing) && (
                <Analysis
                  {...this.state.analysis}
                  analyzing={this.state.analyzing}
                />
              )}
          </div>
        </div>

        <LibraryModal
          onClick={(level) => {
            this.setState({ libraryOpen: false });
            this.load(level);
          }}
          open={this.state.libraryOpen}
          onClose={() => this.setState({ libraryOpen: false })}
        />
      </div>
    );
  }
}

function Analysis(props) {
  const BASE_CLASS = "builder__tools__analysis";
  if (props.analyzing) {
    return (
      <div style={{ margin: "30px" }}>
        <div class="lds-spinner">
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
        </div>
      </div>
    );
  }
  if (props.won) {
    return (
      <div className={BASE_CLASS + " " + (BASE_CLASS + "--won")}>You win!</div>
    );
  }
  if (props.tooHard) {
    return (
      <div className={BASE_CLASS + " " + (BASE_CLASS + "--hard")}>
        At least {props.moveCount} moves
      </div>
    );
  }
  if (props.impossible) {
    return (
      <div className={BASE_CLASS + " " + (BASE_CLASS + "--impossible")}>
        No solution
      </div>
    );
  }
  const nextMove = props.path[0].toString();
  const moveSymbols = {
    "0,1": "→",
    "1,0": "↓",
    "0,-1": "←",
    "-1,0": "↑",
  };
  return (
    <div className={BASE_CLASS}>
      {props.moveCount} moves {moveSymbols[nextMove]}
    </div>
  );
}
