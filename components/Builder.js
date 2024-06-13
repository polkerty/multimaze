import React, { Component } from "react";
import { faQuestionCircle, faTrophy } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Level, { Cell, TOKEN } from "./level";
import Leaderboard from "./leaderboard";
import { Board } from "../utils/logic";
import Celebrate from "../utils/celebrate";
import InputHandler from "../utils/inputHandler";
import LevelConfig from "../utils/levelConfig";
import solver from "../utils/workerManager";

if (typeof window !== "undefined") window.solver = solver;

function cloneDeep(obj) {
  return JSON.parse(JSON.stringify(obj));
}

const LEGAL_TOKEN_PAIRS = [
  [TOKEN.COLLAPSE, TOKEN.COIN],
  [TOKEN.COLLAPSE, TOKEN.BARRIER],
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

    const defaultRows = 5,
      defaultCols = 5;

    this.analysisRequests = [];

    this.state = {
      //TODO: allow loading levels/groups from lib
      rows: defaultRows,
      cols: defaultCols,
      definition: makeBlankDefinition(defaultRows, defaultCols),
      activeToken: TOKEN.WALL,
      version: 0,
      history: [],
      analysis: null,
    };
  }

  componentDidMount() {
    if (typeof window === "undefined") {
      return;
    }
    // TODO: load state from URL (also update URL with state)
  }

  clickHandler(props) {
    this.updateTokenAtPosition(props.row, props.col);
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

  applyStateChange(definition) {
    this.state.history.push(this.state.definition);
    this.setState({ definition, version: this.state.version + 1 });

    // We would also like to analyze the position using our web worker.
    // But we need to disregard any previous analysis requests.

    const pos = this.analysisRequests.length;
    this.analysisRequests.push(
      window.solver.solve(definition).then((result) => {
        console.log("Got result!", result);
        if (this.analysisRequests.length !== pos + 1) {
          // Another request has been made since we initiated this request; abort.
          return;
        }
        this.setState({ analysis: result });
      })
    );
  }

  render() {
    return (
      <div className={"builder-wrap"}>
        <h1 className={"game-title"}>Create Your Own Level</h1>

        {/* TODO: Allow entering level + description */}

        <div className="builder">
          <div className="builder__main-pane">
            <Level
              definition={this.state.definition}
              inputHandler={this.inputHandler}
              key={this.state.version}
              onclick={this.clickHandler.bind(this)}
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
            {this.state.analysis && <Analysis {...this.state.analysis} />}
          </div>
        </div>
      </div>
    );
  }
}

function Analysis(props) {
  const BASE_CLASS = "builder__tools__analysis";
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
  return (
    <div className={BASE_CLASS}>{props.moveCount} moves</div>
  );
}
