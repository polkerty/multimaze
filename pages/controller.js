import React, {Component} from 'react';
import {defaultLevels} from './levelConfig';
import Level from "./level";

export default class Controller extends Component {
    constructor(props) {
        super(props);

        this.state = {
            levels: defaultLevels,
            currentLevel: 0
        }
    }

    getCurrentLevel() {
        return this.state.levels[this.state.currentLevel];
    }

    render() {
        const level = this.getCurrentLevel();
        return (<div className={"level-wrap"}>
            <h1>Multimaze Level {this.state.currentLevel + 1}: {level.name}</h1>
            <Level key={level.id} id={level.id} name={level.name} definition={level.definition} />
        </div>)
    }
}
