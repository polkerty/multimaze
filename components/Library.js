import React, { Component } from "react";
import LevelConfig from "../utils/levelConfig";
import Sequence from "./Sequence";

const { puzzles, groups } = require("../components/levels.json");

class Group {
  constructor(name) {
    this.name = name;
    this.levels = [];
  }
  addPuzzle(level) {
    this.levels.push(level);
  }
}

function makeDefaultLibrary() {
  const lib = [];
  for ( const name of groups ) {
    lib.push(new Group(name));
  }
  for ( let index = 0; index < puzzles.length; ++index ) {
    const { name, definition, groups, description } = puzzles[index];
    for ( const group of groups ) {
        lib[group].addPuzzle(new LevelConfig(index, name, definition, groups, description))
    }
  }
  return lib;
}

const lib = makeDefaultLibrary();

export default class Library extends Component {
  constructor(props) {
    super(props);

  }

  render() {
    return (
      <div className={"library"}>
        {lib.map((group) => {
          return (
            <div className="shelf">
              <h2>{group.name}</h2>
              <Sequence levels={group.levels} />
            </div>
          );
        })}
      </div>
    );
  }
}
