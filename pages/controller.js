import React, {Component} from 'react';
import Level from "./level";

class InputHandler {
    constructor() {

        this.handlers = {};
        if (typeof window === 'undefined') return;

        const self = this;
        window.addEventListener('keydown', function (e) {
            switch(e.key) {
                case 'ArrowLeft':
                    self.emit('left');
                    break;
                case 'ArrowRight':
                    self.emit('right');
                    break;
                case 'ArrowUp':
                    self.emit('up');
                    break;
                case 'ArrowDown':
                    self.emit('down');
                    break;
                case 'r':
                    self.emit('restart');
                    break;
                case 'w':
                    self.emit('win');
                    break;
                default:
                // Life is good, take it easy
            }
        })

    }

    clearAll() {
        this.handlers = {};
    }

    emit(event, data = null) {
        if (this.handlers[event]) {
            for (const handler of this.handlers[event]) {
                handler(data)
            }
        }
    }

    on(event, fn) {
        // Add an event handler
        this.handlers[event] = this.handlers[event] || [];
        this.handlers[event].push(fn);
    }

    off(event, fn) {
        // Delete the event handler (should be called when level is exited)
        if (!this.handlers[event]) return;
        let index = this.handlers[event].indexOf(fn);
        if (index === -1) return;
        this.handlers[event].splice(index, 1);
    }


}

class LevelConfig {
    constructor(id, name, definition) {
        this.name = name;
        this.definition = definition;
    }
}

const levelDefinitions = require('./levels.json');
const defaultLevels = levelDefinitions.map(({name, definition}, index) => new LevelConfig(index, name, definition));


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
            <h1 style={{display: "flex", justifyContent: "center"}}>Multimaze Level {this.state.currentLevel + 1}: {level.name}</h1>
            <Level key={this.state.gameCount} levelId={level.id} name={level.name} definition={level.definition} inputHandler={this.inputHandler} announceVictory={this.onCurrentLevelWin.bind(this)} />
        </div>)
    }
}

