import React, {Component} from "react";
import {Board} from "../utils/logic";

export const TOKEN = {
    WALL: 1,
    PLAYER1: 2,
    FINISH1: 3,
    DEATH: 4,
    COLLAPSE: 5,
    BARRIER: 6,
    COIN: 7
}

const CODE_TO_TOKEN = Object.fromEntries(Object.entries(TOKEN).map(([a, b]) => [b, a]));

function softDeepCopy(object) {
    if (!object) return object;
    return JSON.parse(JSON.stringify(object));
}

export default class Level extends Component {
    constructor(props) {
        super(props);

        const grid = softDeepCopy(props.definition || []);
        this.board = new Board({grid}, {
            onchange: () => this.onchange(),
            onwin: () => this.win()
        });
        this.state = {
            board: grid,
            deathByes: [],
        }
    }

    onchange() {
        this.setState(this.board.state);
    }

    componentDidMount() {
        this.board.restart();

        this.props.inputHandler.clearAll();
        this.props.inputHandler.on('left', () => this.board.move(0, -1));
        this.props.inputHandler.on('right', () => this.board.move(0, 1));
        this.props.inputHandler.on('up', () => this.board.move(-1, 0));
        this.props.inputHandler.on('down', () => this.board.move(1, 0));
        this.props.inputHandler.on('restart', () => this.board.restart());
        this.props.inputHandler.on('win', () => this.win());
        this.props.inputHandler.on('ai', () => this.board.aiSimple());
    }

    render() {

        return <div className={"level-grid"}>
            {
                this.state.board.map((row, index) => (<div key={index} className={"level-row"}>
                    {
                        row.map((cell, index) => <Cell key={index} def={cell}/>)
                    }
                </div>))
            }
        </div>
    }


    win() {
        this.props.announceVictory();
    }

    componentWillUnmount() {
        this.props.inputHandler.clearAll();
    }

}

export function Cell(props) {

    const style = {};
    if (props.size) {
        style.width = props.size + 'px';
        style.height = props.size + 'px';
    }
    return <div style={style} className={"level-cell" + (props.size ? ' level-cell--sized' : '')}>
        <div className={"level-cell__spacer"}/>
        {
            props.def.map((code, index) => <div key={index}
                                                className={"level-token level-token--" + CODE_TO_TOKEN[code]}>
                <div className={"level-cell__spacer"}/>
            </div>)
        }
    </div>
}
