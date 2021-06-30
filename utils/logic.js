import {TOKEN} from "../pages/level";

function softDeepCopy(object) {
    if (!object) return object;
    return JSON.parse(JSON.stringify(object));
}

export class Board {
    constructor({grid, deathByes}, {onchange, onwin}) {

        this.definition = grid;
        this.state = {
            board: grid,
            deathByes: deathByes || []
        };

        this.onchange = onchange;
        this.onwin = onwin;
    }

    aiSimple(maxIter = 1000000) {
        // Let's get all possible moves.

        console.log("Neighbors: ", this.getNeighbors());

        const seen = new Set();
        const memo = {[this.getHash()]: []}

        const queue = [[this, []]];

        let best = {
            target: null,
            path: []
        }

        let i = 0;
        while (queue.length && i++ < maxIter) {
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
                if (!(nHash in memo) || (memo[nHash].length > path.length + 1)) {
                    memo[nHash] = path.concat([delta]);
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

    }

    animateSequence(seq, wait=1000) {
        if ( !seq.length) return;
        const move = seq[0];
        this.move(move[0], move[1]);
        setTimeout(()=>this.animateSequence(seq.slice(1), wait), wait)
    }

    win() {
        if (this.onwin) {
            this.onwin()
        }
    }

    hash(str, seed = 0) {
        return str;
        let h1 = 0xdeadbeef ^ seed, h2 = 0x41c6ce57 ^ seed;
        for (let i = 0, ch; i < str.length; i++) {
            ch = str.charCodeAt(i);
            h1 = Math.imul(h1 ^ ch, 2654435761);
            h2 = Math.imul(h2 ^ ch, 1597334677);
        }
        h1 = Math.imul(h1 ^ (h1 >>> 16), 2246822507) ^ Math.imul(h2 ^ (h2 >>> 13), 3266489909);
        h2 = Math.imul(h2 ^ (h2 >>> 16), 2246822507) ^ Math.imul(h1 ^ (h1 >>> 13), 3266489909);
        return 4294967296 * (2097151 & h2) + (h1 >>> 0);
    }

    getHash() {
        return this.hash(JSON.stringify(this.state));
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


    move(dx, dy, soft = false) {
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

        if (soft) {
            return new Board({
                grid: newBoard,
                deathByes: deathByes
            }, {})
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
