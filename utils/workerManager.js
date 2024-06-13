class SolveWorkerManager {
    constructor() {
        if ( typeof window !== 'undefined' && window.Worker ) {
            this.worker = new Worker('solveWorker.js');
            this.worker.po
        }
    }
}

const solver = new SolveWorkerManager();
export default solver;