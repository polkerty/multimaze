import React, {Component} from 'react';
import {faQuestionCircle, faTrophy} from '@fortawesome/free-solid-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import Level from './level'
import Leaderboard from "./leaderboard";
import {Board} from "../utils/logic";
import Celebrate from "../utils/celebrate";
import InputHandler from '../utils/inputHandler';

class LevelConfig {
    constructor(id, name, definition, groups, description) {
        this.id = id;
        this.name = name;
        this.definition = definition;
        this.groups = groups;
        this.description = description || '';
    }
}

function makeBlankDefinition(rows, cols) {
    const definition = [];
    for ( let i = 0; i < rows; ++i ) {
        const row = [];
        for ( let j  = 0; j < cols; ++j) {
            row.push([]);
        }
        definition.push(row);
    }
    return definition;
}

const {puzzles, groups} = require('./levels.json');
const defaultLevels = puzzles.map(({
                                       name,
                                       definition,
                                       groups,
                                       description
                                   }, index) => new LevelConfig(index, name, definition, groups, description));

export default class Builder extends Component {
    constructor(props) {
        super(props);

        this.inputHandler = new InputHandler();

        const defaultRows = 5, defaultCols = 5;


        this.state = {
            //TODO: allow loading levels/groups from lib
            rows: defaultRows,
            cols: defaultCols,
            definition: makeBlankDefinition(defaultRows, defaultCols)
        }

    }

    componentDidMount() {
        if (typeof window === 'undefined') {
            return;
        }
        // TODO: load state from URL (also update URL with state)
    }


    render() {

        return (<div className={"level-wrap"}>
            <h1 className={"game-title"}>Create Your Own Level
            </h1>

            { /* TODO: Allow entering level + description */ }

            <Level definition={this.state.definition} inputHandler={this.inputHandler} />
        </div>)
    }

    getCurrentGameId() {
        const level = this.getCurrentLevel();
        return new Board({grid: level.definition}, {}).getInitialHash();
    }
}
