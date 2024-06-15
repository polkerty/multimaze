import SolveWorker from 'worker-loader!./solveWorker.js';


class SolveWorkerManager {
    constructor() {
        this.setup();
    }

    setup() {
        if ( typeof window !== 'undefined' && window.Worker ) {
            this.worker = new SolveWorker();
            this.worker.onmessage = e => {
                const messageId = e.data.messageId;
                if ( this.messageBuffer[messageId] ) {
                    if ( e.data.error ) {
                        this.messageBuffer[messageId].reject(e.data.payload);
                    } else {
                        this.messageBuffer[messageId].resolve(e.data.payload);
                    }
                } 
            }
        }

        this.messageBuffer = {};
        
        this.messageId = 0;
    }

    async message(payload) {
        const messageId = this.messageId++;
        const listener = new Promise((resolve, reject) => {
            this.messageBuffer[messageId] = { resolve, reject }
        })
        this.worker.postMessage({ payload, messageId });
        return listener;
    }

    async solve(definition, deathByes) {
        return this.message({ action: 'solve', definition, deathByes })
    }

    refresh() {
        this.worker.terminate();
        this.setup();
    }
}

const solver = new SolveWorkerManager();
export default solver;