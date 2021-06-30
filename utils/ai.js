import {TOKEN} from "../pages/level";

function softDeepCopy(object) {
    if (!object) return object;
    return JSON.parse(JSON.stringify(object));
}

export class Board {
    constructor(grid, {onchange, onwin}) {

        this.definition = grid;
        this.state = {
            board: grid,
            deathBytes: []
        };

        this.onchange = onchange;
        this.onwin = onwin;
    }

    aiSimple() {

    }

    win() {
        if (this.onwin) {
            this.onwin()
        }
    }


    move(dx, dy) {
        let newBoard = softDeepCopy(this.state.board);
        let playerSquares = this.getPlayerSquares();

        let deathByes = [];

        for (const [x, y] of playerSquares) {
            while (newBoard[x][y].includes(TOKEN.PLAYER1)) {
                newBoard[x][y].splice(newBoard[x][y].indexOf(TOKEN.PLAYER1), 1)
            }
        }
        for (const [x, y] of playerSquares) {
            let newX = x + dx, newY = y + dy;
            if (!this.isValidPosition(newX, newY)) {
                newBoard[x][y].push(TOKEN.PLAYER1)
                continue
            }

            let newContents = softDeepCopy(this.state.board[x][y]);
            while (newContents.includes(TOKEN.PLAYER1)) {
                newContents.splice(newContents.indexOf(TOKEN.PLAYER1), 1);
            }

            if (this.canAcceptPlayer(newX, newY)) {

            } else {
                newContents.push(TOKEN.PLAYER1)
            }
            if (newBoard[x][y].includes(TOKEN.PLAYER1) && !newContents.includes(TOKEN.PLAYER1)) {
                newContents.push(TOKEN.PLAYER1)
            }

            newBoard[x][y] = newContents;
            //removeDuplicatePlayers(newContents)
            let [contents, needDeathBye] = this.handleAttemptedMove(newX, newY);
            //removeDuplicatePlayers(contents)
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

        if (this.hasWon()) {
            this.win();
        }
    }

    setState(state) {
        this.state = Object.assign(this.state, state);
        if (this.onchange) {
            this.onchange();
        }
    }

    getPlayerSquares() {
        let squares = [];
        for (let i = 0; i < this.state.board.length; ++i) {
            for (let j = 0; j < this.state.board[i].length; ++j) {
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

    removeDuplicatePlayers(arr) {
        if (arr.indexOf(TOKEN.PLAYER1) !== arr.lastIndexOf(TOKEN.PLAYER1)) {
            arr.splice(arr.indexOf(TOKEN.PLAYER1), 1)
        }
    }

    removePlayers(arr) {
        while (arr.indexOf(TOKEN.PLAYER1) > -1) {
            arr.splice(arr.indexOf(TOKEN.PLAYER1), 1)
        }
    }

    handleAttemptedMove(x, y) {
        let tokens = softDeepCopy(this.state.board[x][y]);
        if (this.canAcceptPlayer(x, y)) {
            tokens.push(TOKEN.PLAYER1);
        }
        tokens = tokens.filter(x => x !== TOKEN.BARRIER);
        tokens = tokens.filter(x => x !== TOKEN.COIN);

        let turnDead = false;

        if (tokens.includes(TOKEN.COLLAPSE) && this.canAcceptPlayer(x, y)) {
            tokens = tokens.filter(x => x !== TOKEN.COLLAPSE);
            tokens.push(TOKEN.DEATH);
            turnDead = true;
        }


        return [[...tokens], turnDead];
    }

    isDead() {
        for (let i = 0; i < this.state.board.length; ++i) {
            for (let j = 0; j < this.state.board[i].length; ++j) {
                if (this.state.deathByes.some(([x, y]) => x === i && y === j)) continue;
                if (this.state.board[i][j].includes(TOKEN.DEATH) && this.state.board[i][j].includes(TOKEN.PLAYER1)) return true;
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
            board: softDeepCopy(this.definition || []),
            deathByes: [],
        })
    }

}

