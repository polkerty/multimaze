import React, {Component} from "react";
import {Board} from "../utils/logic";
import {faUndo, faTimes} from '@fortawesome/free-solid-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'

export const TOKEN = {
    WALL: 1,
    PLAYER1: 2,
    FINISH1: 3,
    DEATH: 4,
    COLLAPSE: 5,
    BARRIER: 6,
    COIN: 7,
    PLAYER2: 8,
    REVERSER: 9
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
            onwin: (props) => this.win(props),
            onundo: () => this.onundo()
        });
        this.state = {
            board: grid,
            deathByes: [],
            startTime: new Date().getTime()
        }
    }

    onchange() {
        this.setState(this.board.state);
    }

    componentDidMount() {
        this.board.restart();

        this.props.inputHandler.clearAll();
        this.props.inputHandler.on('left', () => this.board.availableForMoves() && this.board.move(0, -1));
        this.props.inputHandler.on('right', () => this.board.availableForMoves() && this.board.move(0, 1));
        this.props.inputHandler.on('up', () => this.board.availableForMoves() && this.board.availableForMoves() && this.board.move(-1, 0));
        this.props.inputHandler.on('down', () => this.board.availableForMoves() && this.board.move(1, 0));
        this.props.inputHandler.on('restart', () => this.board.availableForMoves() && this.board.restart());
        this.props.inputHandler.on('win', () => this.board.availableForMoves() && this.win({
            isSkip: 1
        }));
        this.props.inputHandler.on('back', () => this.board.availableForMoves() && this.win({
            retreat: 1,
            isSkip: 1
        }));
        this.props.inputHandler.on('ai', () => this.board.aiSimple());
        this.props.inputHandler.on('undo', () => this.board.availableForMoves() && this.board.undo());
    }

    render() {

        return (<>
            <div className={"level-grid"}>
                {
                    this.state.board.map((row, index) => (<div key={index} className={"level-row"}>
                        {
                            row.map((cell, index) => <Cell key={index} def={cell}/>)
                        }
                    </div>))
                }
            </div>
            <div className={"level-controls"}>
                {this.board.stack.length ?
                    <button className={"undo-button"} onClick={() => this.board.undo()}><FontAwesomeIcon icon={faUndo}/>
                    </button> : ''}
            </div>
        </>)
    }

    onundo() {

    }


    win(props =
            {}
    ) {
        props = Object.assign({
            isSkip: 0,
            retreat: 0,
            didCheat: 0,
            totalMoves: -1,
            didUndo: 0
        }, props);
        this.props.announceVictory({
            gameId: this.board.getInitialHash(),
            isSkip: props.isSkip,
            retreat: props.retreat,
            startTime: this.state.startTime,
            didCheat: props.didCheat,
            didUndo: props.didUndo,
            runTime: (new Date().getTime() - this.state.startTime) / 1000,
            totalMoves: props.totalMoves
        });
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
