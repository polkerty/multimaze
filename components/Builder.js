import React, { Component } from "react";
import { faQuestionCircle, faTrophy } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Level, { Cell, TOKEN } from "./level";
import Leaderboard from "./leaderboard";
import { Board } from "../utils/logic";
import Celebrate from "../utils/celebrate";
import InputHandler from "../utils/inputHandler";

class LevelConfig {
  constructor(id, name, definition, groups, description) {
    this.id = id;
    this.name = name;
    this.definition = definition;
    this.groups = groups;
    this.description = description || "";
  }
}

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
    <div tabIndex={-1} className={BASE_CLASS + " " + (active ? ACTIVE : "")}>
      <Cell def={type ? [type] : []} onClick={onClick} size={30} />
    </div>
  );
}
export default class Builder extends Component {
  constructor(props) {
    super(props);

    this.inputHandler = new InputHandler();

    const defaultRows = 5,
      defaultCols = 5;

    this.state = {
      //TODO: allow loading levels/groups from lib
      rows: defaultRows,
      cols: defaultCols,
      definition: makeBlankDefinition(defaultRows, defaultCols),
      activeToken: TOKEN.WALL,
    };
  }

  componentDidMount() {
    if (typeof window === "undefined") {
      return;
    }
    // TODO: load state from URL (also update URL with state)
  }

  clickHandler(props) {
    console.log(props.row, props.col, props);
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
          </div>
        </div>
      </div>
    );
  }

}
