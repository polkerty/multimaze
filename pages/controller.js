import React, {Component} from 'react';
import {defaultLevels} from './levelConfig';
import Level from "./level";
import InputHandler from "./inputHandler";

export default class Controller extends Component {
    constructor(props) {
        super(props);

        this.inputHandler = new InputHandler();

        this.state = {
            levels: defaultLevels,
            currentLevel: 0,
            gameCount: 0
        }
    }

    getCurrentLevel() {
        return this.state.levels[this.state.currentLevel];
    }

    onCurrentLevelWin() {
        this.setState({
            currentLevel: (this.state.currentLevel + 1 ) % this.state.levels.length,
            gameCount: this.state.gameCount + 1
        })
    }

    render() {
        const level = this.getCurrentLevel();
        return (<div className={"level-wrap"}>
            <h1>Multimaze Level {this.state.currentLevel + 1}: {level.name}</h1>
            <Level key={this.state.gameCount} levelId={level.id} name={level.name} definition={level.definition} inputHandler={this.inputHandler} announceVictory={this.onCurrentLevelWin.bind(this)} />
        </div>)
    }
}
