import React, { Component } from "react";
import Level from "../components/level";

export default class Sequence extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className={"sequence-wrap"}>
        {this.props.levels.map((level) => {
          return (
            <div className="sequence">
              <Level
                key={level.id}
                levelId={level.id}
                name={level.name}
                definition={level.definition}
              />
            </div>
          );
        })}
      </div>
    );
  }
}
