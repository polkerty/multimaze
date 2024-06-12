class InputHandler {
    constructor() {

        this.handlers = {};
        if (typeof window === 'undefined') return;

        const self = this;
        window.addEventListener('keydown', function (e) {
            switch (e.key) {
                case 'f':
                    self.emit('swap')
                    break;
                case 'ArrowLeft':
                case 'a':
                    self.emit('left');
                    e.preventDefault();
                    break;
                case 'ArrowRight':
                case 'd':
                    self.emit('right');
                    e.preventDefault();
                    break;
                case 'ArrowUp':
                case 'w':
                    self.emit('up');
                    e.preventDefault();
                    break;
                case 'ArrowDown':
                case 's':
                    self.emit('down');
                    e.preventDefault();
                    break;
                case 'r':
                    self.emit('restart');
                    break;
                case 'X':
                    console.log("X? ", e.shiftKey);
                    if (e.shiftKey) {
                        self.emit('win');
                    }
                    break;
                case 'Z':
                    if (e.shiftKey) {
                        self.emit('back');
                    }
                    break;
                case 'O':
                    if (e.shiftKey) {
                        self.emit('ai');
                    }
                    break;
                case 'u':
                    self.emit('undo')
                    break;
                default:
                // Life is good, take it easy
            }
        })

        // https://stackoverflow.com/questions/2264072/detect-a-finger-swipe-through-javascript-on-the-iphone-and-android
        document.addEventListener('touchstart', handleTouchStart, false);
        document.addEventListener('touchmove', handleTouchMove, false);

        var xDown = null;
        var yDown = null;

        function getTouches(evt) {
            return evt.touches ||             // browser API
                evt.originalEvent.touches; // jQuery
        }

        function handleTouchStart(evt) {
            const firstTouch = getTouches(evt)[0];
            xDown = firstTouch.clientX;
            yDown = firstTouch.clientY;
        }

        function handleTouchMove(evt) {
            if (!xDown || !yDown) {
                return;
            }

            var xUp = evt.touches[0].clientX;
            var yUp = evt.touches[0].clientY;

            var xDiff = xDown - xUp;
            var yDiff = yDown - yUp;

            if (Math.abs(xDiff) > Math.abs(yDiff)) {/*most significant*/
                if (xDiff > 0) {
                    self.emit('left');
                } else {
                    self.emit('right');
                }
            } else {
                if (yDiff > 0) {
                    self.emit('up');
                } else {
                    self.emit('down');
                }
            }
            /* reset values */
            xDown = null;
            yDown = null;
        }

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

export default InputHandler;