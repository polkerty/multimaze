import SolveWorker from 'worker-loader!./solveWorker.js';


class SolveWorkerManager {
    constructor() {
        if ( typeof window !== 'undefined' && window.Worker ) {
            this.worker = new SolveWorker();
            this.worker.onmessage = e => {
                const messageId = e.data.messageId;
                if ( this.messageBuffer[messageId] ) {
                    this.messageBuffer[messageId].resolve(e.data.payload);
                } 
            }
            this.worker.onmessageerror = e => {
                const messageId = e.data.messageId;
                if ( this.messageBuffer[messageId] ) {
                    
                } 
            }
        }

        this.messageBuffer = {};
        
        this.messageId = 0;
    }

    async message(payload) {
        payload.messageId = this.messageId++;
        const listener = new Promise((res, rej) => {
            this.messageBuffer[payload.messageId] = { res, rej}
        })
        this.worker.postMessage({ payload, messageId });
    }

    async solve(definition) {
        await this.message({ action: 'solve', definition })
    }
}

const solver = new SolveWorkerManager();
export default solver;