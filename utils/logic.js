import {TOKEN} from "../components/level";
import btoa from "btoa";

function softDeepCopy(object) {
    if (!object) return object;
    return JSON.parse(JSON.stringify(object));
}

function fastCopy(arr) {
    let newArr = new Array(arr.length);
    for (let i = 0; i < arr.length; ++i) {
        newArr[i] = new Array(arr[i].length);
        for (let j = 0; j < newArr[i].length; ++j) {
            newArr[i][j] = arr[i][j].slice();
        }
    }
    return newArr;
}

export class Board {
    constructor({grid, deathByes}, options = {}) {

        this.definition = grid;
        this.state = {
            board: grid,
            deathByes: deathByes || []
        };

        this.stack = [];

        this.cachedPlayerSquares = options.cachedPlayerSquares || null;
        this.cachedIsDead = options.hasOwnProperty('cachedIsDead') ? options.cachedIsDead : null;
        this.cachedHasWon = options.hasOwnProperty('cachedHasWon') ? options.cachedHasWon : null;
        this.cachedRepr = options.hasOwnProperty('cachedRepr') ? options.cachedRepr : null;

        // if (this.cachedRepr && this.cachedRepr.flat().join('') !== this.repr().flat().join('')) {
        //     console.log("Mismatch", this.cachedRepr, this.repr());
        //     throw "up";
        // }

        this.totalMoves = 0;

        this.onchange = options.onchange;
        this.onwin = options.onwin;
        this.onrestart = options.onrestart;

        this.aiLoop = 0;

        this.didCheat = 0;
        this.didUndo = 0;
    }

    aiSimple(maxIter = 1000000) {

        this.didCheat = 1;

        if (this.aiLoop) {
            clearTimeout(this.aiLoop);
            this.aiLoop = null;
            return;
        }
        // Let's get all possible moves.

        const startTime = new Date().getTime();
        console.log("Neighbors: ", this.getNeighbors());

        const seen = new Set();
        const memo = {[this.getHash()]: 0}

        const queue = [[this, []]];

        let best = {
            target: null,
            path: []
        }

        let i = 0;
        while (queue.length && i++ < maxIter) {

            if (i > 50000 && best.target) break;

            const [next, path] = queue.pop();
            const hash = next.getHash();
            if (seen.has(hash)) {
                continue;
            }
            if (next.hasWon() && (!best.target || path.length < best.path.length)) {
                best = {
                    target: next,
                    path: path
                }
            }

            seen.add(hash);
            const neighbors = next.getNeighbors();
            for (const [delta, n] of neighbors) {
                const nHash = n.getHash();
                const m = memo[nHash];
                if (!m || (m > path.length + 1)) {
                    memo[nHash] = path.length + 1;
                    queue.push([n, path.concat([delta])]);
                }
            }
        }

        console.log(memo, Object.values(memo).length, best, best.target?.hasWon());

        if (best.target) {
            this.animateSequence(best.path);
            // this.move(best.path[0][0], best.path[0][1]);
        } else {
            alert('AI not available for this level');
        }

        console.log("AI runtime (sec): ", (new Date().getTime() - startTime) / 1000);

    }

    animateSequence(seq, wait = 300) {
        if (!seq.length) {
            clearTimeout(this.aiLoop);
            this.aiLoop = null;
            return;
        }
        const move = seq[0];
        this.move(move[0], move[1]);
        this.aiLoop = setTimeout(() => this.animateSequence(seq.slice(1), wait), wait)
    }

    win() {
        if (this.onwin) {
            this.onwin({
                didCheat: this.didCheat,
                didUndo: this.didUndo,
                totalMoves: this.totalMoves
            })
        }
    }

    hash(str, seed = 0) {
        return str;
    }

    getHash() {
        // return this.state.board.toString();
        let h = '';
        for (const row of this.repr()) {
            for (const char of row) {
                h += char;
            }
        }
        return h;
        // return this.hash(JSON.stringify(this.state));
    }

    repr() {
        if (this.cachedRepr) return this.cachedRepr.map(row => row.map(cell => cell));
        return this.state.board.map(row => row.map(cell => this.cellRepr(cell)))
    }

    cellRepr(items) {
        let bitmask = 0;
        for (const item of items) {
            bitmask |= 1 << item;
        }
        return String.fromCharCode(bitmask);
    }

    getInitialHash() {
        return btoa(JSON.stringify({
            board: this.definition,
            deathByes: 0
        }))
    }


    getNeighbors() {
        const possibleDeltas = [[-1, 0], [1, 0], [0, -1], [0, 1]];

        let seen = new Set();

        let neighbors = possibleDeltas.map(([dx, dy]) => [[dx, dy], this.move(dx, dy, true)]);
        neighbors = neighbors.filter(([, b]) => {
            const hash = b.getHash();
            if (seen.has(hash)) return false;
            if (b.isDead()) return false;
            seen.add(hash);
            return true;
        })


        return neighbors;

    }

    availableForMoves() {
        return !this.aiLoop;
    }

    removePlayersFromArray(arr) {
        let newArr = [];
        for (const t of arr) {
            if (t === TOKEN.PLAYER1 || t === TOKEN.PLAYER2) continue;
            newArr.push(t);
        }
        return newArr;
    }

    mapType(type, isFlipped) {
        return !isFlipped ? type : type === TOKEN.PLAYER1 ? TOKEN.PLAYER2 : TOKEN.PLAYER1;
    }

    move(dx, dy, soft = false) {
        let newBoard = fastCopy(this.state.board);
        let [playerSquares, coinCount] = this.getPlayerSquares();

        let deathByes = [];

        for (const [x, y, type] of playerSquares) {
            newBoard[x][y] = this.removePlayersFromArray(newBoard[x][y]);
        }

        let i = 0;

        let newPlayerSquares = [];

        let repr = this.repr(true);

        let affectedSquaresApprox = [];

        for (const [x, y, type] of playerSquares) {
            let idx = type === TOKEN.PLAYER1 ? dx : dx * -1;
            let idy = type === TOKEN.PLAYER1 ? dy : dy * -1;

            let newX = x + idx, newY = y + idy;
            if (!this.isValidPosition(newX, newY)) {
                newBoard[x][y].push(type)
                newPlayerSquares.push([x, y, type]);
                continue
            }
            affectedSquaresApprox.push([newX, newY]);


            let newContents = this.removePlayersFromArray(this.state.board[x][y]);

            let [canAccept, isFlipped, hasCoin] = this.canAcceptPlayer(newX, newY, type);

            if (canAccept) {
                const newType = this.mapType(type, isFlipped);
                newPlayerSquares.push([newX, newY, newType]);
                if (hasCoin) coinCount--;
            } else {
                newContents.push(type)
                newPlayerSquares.push([x, y, type]);
            }
            if (newBoard[x][y].includes(type) && !newContents.includes(type)) {
                newContents.push(type)
            }

            newBoard[x][y] = newContents;
            let [contents, needDeathBye] = this.handleAttemptedMove(newX, newY, type);
            newBoard[newX][newY] = contents;
            if (needDeathBye) {
                deathByes.push([newX, newY]);
            }

            ++i;
        }


        if (soft) {
            // Careful bookkeeping buys us some performance here...
            let isDead = false;
            let hasWon = coinCount === 0;

            let cachedPlayerSquares = [];

            for (let e of playerSquares.concat(affectedSquaresApprox)) {
                repr[e[0]][e[1]] = this.cellRepr(newBoard[e[0]][e[1]]);
            }
            for (let e of newPlayerSquares) {
                if (cachedPlayerSquares.find(x => x[0] === e[0] && x[1] === e[1] && x[2] === e[2])) continue;
                cachedPlayerSquares.push(e);
                if (this.state.board[e[0]][e[1]].includes(TOKEN.DEATH)) isDead = true;
                if (!this.state.board[e[0]][e[1]].includes(TOKEN.FINISH1)) hasWon = false;
            }

            return new Board({
                grid: newBoard,
                deathByes: deathByes
            }, {
                cachedPlayerSquares: [cachedPlayerSquares, coinCount],
                cachedIsDead: isDead,
                cachedHasWon: hasWon,
                cachedRepr: repr
            })
        }

        this.applyState({
            board: newBoard,
            deathByes: deathByes
        })

    }

    applyState(state) {
        /**
         * A wrapper for setState, but with more book keeping
         */
        this.totalMoves++;
        this.stack.push(softDeepCopy(this.state));

        this.setState(state)

        if (this.isDead()) return this.restart({
            didDie: true
        });

        if (this.hasWon()) {
            this.win();
        }


    }

    undo() {
        if (!this.stack.length) return;
        this.didUndo = 1;
        this.setState(this.stack.pop());
    }

    setState(state) {
        this.state = Object.assign(this.state, state);
        if (this.onchange) {
            this.onchange();
        }
    }

    getPlayerSquares() {
        if (this.cachedPlayerSquares) return this.cachedPlayerSquares; // Careful bookkeeping buys us some optimization

        let coinCount = 0;
        let squares = [];
        for (let i = 0; i < this.state.board.length; ++i) {
            for (let j = 0; j < this.state.board[i].length; ++j) {
                if (this.state.board[i][j].includes(TOKEN.COIN)) ++coinCount;
                let type;
                if (this.state.board[i][j].includes(TOKEN.PLAYER1)) type = TOKEN.PLAYER1;
                else if (this.state.board[i][j].includes(TOKEN.PLAYER2)) type = TOKEN.PLAYER2;
                else continue;
                squares.push([i, j, type]);
            }
        }

        // if (this.cachedPlayerSquares && this.cachedPlayerSquares.toString() !== squares.toString()) console.log(JSON.stringify(this.cachedPlayerSquares), JSON.stringify(squares));
        return [squares, coinCount];
    }

    isValidPosition(x, y) {
        return x >= 0 && y >= 0 && x < this.state.board.length && y < this.state.board[x].length;
    }

    canAcceptPlayer(x, y, type = TOKEN.PLAYER1) {
        let antiType = type === TOKEN.PLAYER1 ? TOKEN.PLAYER2 : TOKEN.PLAYER1;
        let isFlipped = false, hasCoin = false, open = true;
        for (const token of this.state.board[x][y]) {
            if (token === TOKEN.REVERSER) isFlipped = true;
            if (token === TOKEN.COIN) hasCoin = true;
            if (token === TOKEN.WALL || token === TOKEN.BARRIER || token === antiType) open = false;

        }
        return [open, isFlipped, hasCoin];
    }

    handleAttemptedMove(x, y, type = TOKEN.PLAYER1) {
        let tokens = [];
        let [canAccept, isFlipped] = this.canAcceptPlayer(x, y, type);
        if (canAccept) {
            const newPlayer = this.mapType(type, isFlipped);
            tokens.push(newPlayer);
        }
        let turnDead = false;

        for (const token of this.state.board[x][y]) {
            if (token === TOKEN.BARRIER || token === TOKEN.COIN || token === TOKEN.REVERSER) continue;
            if (token === TOKEN.COLLAPSE && canAccept) {
                tokens.push(TOKEN.DEATH);
                turnDead = true;
                continue;
            }
            tokens.push(token);
        }

        return [tokens, turnDead];
    }

    isDead() {
        if (this.cachedIsDead !== null) return this.cachedIsDead;
        for (let i = 0; i < this.state.board.length; ++i) {
            for (let j = 0; j < this.state.board[i].length; ++j) {
                if (this.state.deathByes.some(([x, y]) => x === i && y === j)) continue;
                if (this.state.board[i][j].includes(TOKEN.DEATH) && (this.state.board[i][j].includes(TOKEN.PLAYER1) || this.state.board[i][j].includes(TOKEN.PLAYER2))) return true;
            }
        }
        return false;
    }

    swap() {
        const newBoard = this.state.board.map(row =>
            row.map(cell => {
                    let newCell = [];
                    for (const c of cell) {
                        if (c === TOKEN.PLAYER1) newCell.push(TOKEN.PLAYER2);
                        else if (c === TOKEN.PLAYER2) newCell.push(TOKEN.PLAYER1);
                        else newCell.push(c);
                    }
                    return newCell;
                }
            )
        )
        this.applyState({
            board: newBoard
        })
    }

    hasWon() {
        if (this.cachedHasWon !== null) return this.cachedHasWon;
        let coinCountZero = !this.state.board.flat().some(x => x.includes(TOKEN.COIN));
        let onWinSquares = !this.state.board.flat().some(x => (x.includes(TOKEN.PLAYER1) || x.includes(TOKEN.PLAYER2)) && !x.includes(TOKEN.FINISH1));
        return coinCountZero && onWinSquares;
    }

    restart(props) {
        this.setState({
            board: softDeepCopy(this.definition || []),
            deathByes: [],
        })
        if (this.onrestart) {
            this.onrestart(props);
        }
    }

}
