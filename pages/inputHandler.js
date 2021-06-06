export default function InputHandler() {
    const self = this;

    this.handlers = {};
    if (typeof window !== 'undefined') {

        window.addEventListener('keydown', function (e) {
            switch (e.key) {
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

    self.clearAll = function () {
        self.handlers = {};
    }

    self.emit = function (event, data = null) {
        if (self.handlers[event]) {
            for (const handler of self.handlers[event]) {
                handler(data)
            }
        }
    }

    self.on = function (event, fn) {
        // Add an event handler
        self.handlers[event] = self.handlers[event] || [];
        self.handlers[event].push(fn);
    }

    return self;
}
