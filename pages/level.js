import React, {Component} from "react";

const TOKEN = {
    WALL: 1,
    PLAYER1: 2,
    FINISH1: 3,
    DEATH: 4,
    COLLAPSE: 5,
    BARRIER: 6,
    COIN: 7
}

const CODE_TO_TOKEN = Object.fromEntries(Object.entries(TOKEN).map(([a, b]) => [b, a]));

export default class Level extends Component {
    constructor(props) {
        super(props);
        this.state = {
            board: JSON.parse(JSON.stringify(props.definition)),
            deathByes: [],
        }

        this.props.inputHandler.on('left', () => this.move(0, -1));
        this.props.inputHandler.on('right', () => this.move(0, 1));
        this.props.inputHandler.on('up', () => this.move(-1, 0));
        this.props.inputHandler.on('down', () => this.move(1, 0));
        this.props.inputHandler.on('restart', () => this.restart());
    }

    move(dx, dy) {
        let newBoard = JSON.parse(JSON.stringify(this.state.board));
        let playerSquares = this.getPlayerSquares();

        let deathByes = [];

        for (const [x, y] of playerSquares) {

            let newX = x + dx, newY = y + dy;
            if (!this.isValidPosition(newX, newY)) continue;

            let newContents = JSON.parse(JSON.stringify(this.state.board[x][y]));
            if (this.canAcceptPlayer(newX, newY)) newContents = newContents.filter(x => x !== TOKEN.PLAYER1);

            newBoard[x][y] = newContents;
            let [contents, needDeathBye] = this.handleAttemptedMove(newX, newY);
            newBoard[newX][newY] = contents;
            if (needDeathBye) {
                deathByes.push([newX, newY]);
            }
        }

        this.setState({
            board: newBoard,
            deathByes: deathByes
        })

        if (this.isDead()) return this.restart();

        if ( this.hasWon()) {
            this.win();
        }
    }

    getPlayerSquares() {
        let squares = [];
        for (let i = 0; i < this.state.board.length; ++i) {
            for (let j = 0; j < this.state.board.length; ++j) {
                if (this.state.board[i][j].includes(TOKEN.PLAYER1)) {
                    squares.push([i, j]);
                }
            }
        }
        return squares;
    }

    isValidPosition(x, y) {
        return x >= 0 && y >= 0 && x < this.state.board.length && y < this.state.board[x].length;
    }

    canAcceptPlayer(x, y) {
        return ![TOKEN.WALL, TOKEN.BARRIER].some(z => (this.state.board[x][y].includes(z)));
    }

    handleAttemptedMove(x, y) {
        let tokens = JSON.parse(JSON.stringify(this.state.board[x][y]));
        if (this.canAcceptPlayer(x, y)) {
            tokens.push(TOKEN.PLAYER1);
        }
        tokens = tokens.filter(x => x !== TOKEN.BARRIER);
        tokens = tokens.filter(x => x !== TOKEN.COIN);

        let turnDead = false;

        if (tokens.includes(TOKEN.COLLAPSE)) {
            tokens = tokens.filter(x => x !== TOKEN.COLLAPSE);
            tokens.push(TOKEN.DEATH);
            turnDead = true;
        }


        return [[...new Set(tokens)], turnDead];
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

    isDead() {
        for ( let i = 0; i < this.state.board.length; ++i ){
            for ( let j = 0; j < this.state.board[i].length; ++j ) {
                if ( this.state.deathByes.some(([x, y])=>x === i && y === j)) continue;
                if ( this.state.board[i][j].includes(TOKEN.DEATH) && this.state.board[i][j].includes(TOKEN.PLAYER1)) return true;
            }
        }
        return false;
    }

    hasWon() {
        let coinCountZero = !this.state.board.flat().some(x => x.includes(TOKEN.COIN));
        let onWinSquares = !this.state.board.flat().some(x => x.includes(TOKEN.PLAYER1) && !x.includes(TOKEN.FINISH1));
        return coinCountZero && onWinSquares;
    }

    restart() {
        this.setState({
            board: JSON.parse(JSON.stringify(this.props.definition)),
            deathByes: [],
        })
    }

    win() {
        this.props.announceVictory();
    }

    componentWillUnmount() {
        this.props.inputHandler.clearAll();
    }

}

function Cell(props) {
    return <div className={"level-cell"}>
        {
            props.def.map((code, index) => <div key={index}
                                                className={"level-token level-token--" + CODE_TO_TOKEN[code]}/>)
        }
    </div>
}
