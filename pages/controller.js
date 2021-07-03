import React, {Component} from 'react';
// import Level from "./level";
import {faQuestionCircle, faTrophy} from '@fortawesome/free-solid-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import Help from './help'
import Level from './level'
import Leaderboard from "./leaderboard";
import {Board} from "../utils/logic";

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

class LevelConfig {
    constructor(id, name, definition, groups, description) {
        this.id = id;
        this.name = name;
        this.definition = definition;
        this.groups = groups;
        this.description = description || '';
    }
}

const {puzzles, groups} = require('./levels.json');
const defaultLevels = puzzles.map(({
                                       name,
                                       definition,
                                       groups,
                                       description
                                   }, index) => new LevelConfig(index, name, definition, groups, description));

export default class Controller extends Component {
    constructor(props) {
        super(props);

        this.inputHandler = new InputHandler();

        const initialGroup = 5, initialLevel = 0;

        this.state = {
            levels: defaultLevels.filter(x => x.groups.includes(initialGroup)),
            groups: groups.map((g, index) => ({
                name: g,
                id: index,
                count: defaultLevels.filter((l) => l.groups.includes(index)).length
            })),
            currentLevel: initialLevel,
            currentGroup: initialGroup,
            gameCount: 0,
            showHelp: false,
            tab: "game"
        }

    }

    componentDidMount() {
        if (typeof window !== 'undefined') {
            const initialGroup = typeof localStorage !== 'undefined' && localStorage.mmGroup ? parseInt(localStorage.mmGroup) : 5;
            const initialLevel = typeof localStorage !== 'undefined' && localStorage.mmLevel ? parseInt(localStorage.mmLevel) : 0;
            this.updateGroupAndLevel(initialGroup, initialLevel)
        }
    }

    getCurrentLevel() {
        return this.state.levels[this.state.currentLevel];
    }

    onCurrentLevelWin(props) {
        // Save
        if (!(
            props.totalMoves === -1 // No reason to save completely empty games
        )) {
            fetch('/api/save', {
                method: 'POST',
                body: JSON.stringify({
                    ...props,
                    groupNumber: this.state.currentGroup,
                    levelNumber: this.state.currentLevel,
                })
            })
        }

        const levelShift = props.retreat ? -1 : 1;

        this.updateGroupAndLevel(this.state.currentGroup, (this.state.currentLevel + levelShift + this.state.levels.length) % this.state.levels.length)
    }

    setGroup(groupNumber) {
        this.updateGroupAndLevel(groupNumber, 0);
    }

    updateGroupAndLevel(group, level) {
        localStorage.mmGroup = group;
        localStorage.mmLevel = level;

        let levels = defaultLevels.filter(x => x.groups.includes(group));

        this.setState({
            levels: levels,
            currentGroup: group,
            currentLevel: level,
            gameCount: this.state.gameCount + 1
        })

    }

    toggleHelp() {
        this.setState({
            showHelp: !this.state.showHelp
        })
    }

    setTab(tab) {
        this.setState({
            tab: tab
        });

        return false; // To prevent page from jumping when this method is set as the event handler
    }

    render() {
        const level = this.getCurrentLevel();

        return (<div className={"level-wrap"}>
            <div className={"maze-controls"}>
                {
                    this.state.showHelp ? <Help closeHelp={() => this.toggleHelp()}/> : ''
                }
                <div className={"maze-controls__group-nav"}>
                    {this.state.groups.filter(x => x.count > 0).map(({name, id, count}) => <div
                        key={id}
                        className={"maze-controls__group"}
                        onClick={() => this.setGroup(id)}>{name} <span className={"number-bubble"}>{count}</span>
                    </div>)}
                </div>
                <div className={"maze-controls__spacer"}/>
                <div className={"maze-controls__help"} onClick={() => this.toggleHelp()}>
                    <FontAwesomeIcon icon={faQuestionCircle}/>
                </div>
            </div>
            <h1 className={"game-title"}>{this.state.groups[this.state.currentGroup].name}
                <span style={{marginRight: '10px'}}/>
                {"Level"} {this.state.currentLevel + 1}: {level.name}
                {this.state.tab === 'game'
                    ? <a className="trophy-tab" onClick={() => this.setTab('leaderboard')}
                         href={'#'}> <FontAwesomeIcon icon={faTrophy}/>
                    </a>
                    : <a className={"game-tab"} onClick={() => this.setTab('game')
                    } href={'#'}>Play</a>}
            </h1>
            {level.description.length ? <p style={{textAlign: 'center'}}>{level.description}</p> : ''}

            {this.state.tab === 'game'
                ? <Level key={this.state.gameCount} levelId={level.id} name={level.name} definition={level.definition}
                         inputHandler={this.inputHandler} announceVictory={this.onCurrentLevelWin.bind(this)}/>
                : <Leaderboard levelId={level.id} key={this.state.gameCount} gameId={this.getCurrentGameId()}/>

            }
        </div>)
    }

    getCurrentGameId() {
        const level = this.getCurrentLevel();
        return new Board({grid: level.definition}, {}).getInitialHash();
    }
}
