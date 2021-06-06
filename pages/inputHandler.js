export default class InputHandler {
    constructor() {

        this.handlers = {};
        if (typeof window === 'undefined') return;

        const self = this;
        window.addEventListener('keydown', function (e) {
            switch(e.key) {
                case 'ArrowLeft':
                    self.emit('left');
                    break;
                case 'ArrowRight':
                    self.emit('right');
                    break;
                case 'ArrowUp':
                    self.emit('up');
                    break;
                case 'ArrowDown':
                    self.emit('down');
                    break;
                case 'r':
                    self.emit('restart');
                    break;
                case 'w':
                    self.emit('win');
                    break;
                default:
                    // Life is good, take it easy
            }
        })

    }

    clearAll() {
        this.handlers = {};
    }

    emit(event, data = null) {
        if (this.handlers[event]) {
            for (const handler of this.handlers[event]) {
                handler(data)
            }
        }
    }

    on(event, fn) {
        // Add an event handler
        this.handlers[event] = this.handlers[event] || [];
        this.handlers[event].push(fn);
    }

    off(event, fn) {
        // Delete the event handler (should be called when level is exited)
        if (!this.handlers[event]) return;
        let index = this.handlers[event].indexOf(fn);
        if (index === -1) return;
        this.handlers[event].splice(index, 1);
    }


}
