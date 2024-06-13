import SolveWorker from 'worker-loader!./solveWorker.js';


class SolveWorkerManager {
    constructor() {
        if ( typeof window !== 'undefined' && window.Worker ) {
            this.worker = new SolveWorker();
            this.worker.onmessage = e => {
                console.log("Message: ", e);
            }
        }
    }
}

const solver = new SolveWorkerManager();
export default solver;