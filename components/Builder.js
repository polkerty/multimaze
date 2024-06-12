import React, {Component} from 'react';
import {faQuestionCircle, faTrophy} from '@fortawesome/free-solid-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import Level from './level'
import Leaderboard from "./leaderboard";
import {Board} from "../utils/logic";
import Celebrate from "../utils/celebrate";
import InputHandler from '../utils/inputHandler';

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

export default class Builder extends Component {
    constructor(props) {
        super(props);

        this.inputHandler = new InputHandler();

        const initialGroup = 0, initialLevel = 0;

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
            tab: "game"
        }

    }

    componentDidMount() {
        if (typeof window === 'undefined') {
            return;
        }
        const queryParams = new URLSearchParams(window.location.search);
        const queryGroup = queryParams.get('group') ? parseInt(queryParams.get('group')) : undefined;
        const queryLevel = queryParams.get('level') ? parseInt(queryParams.get('level')) : undefined;
        const locallyStoredGroup = typeof localStorage !== 'undefined' && localStorage.mmGroup ? parseInt(localStorage.mmGroup) : undefined;
        const locallyStoredLevel = typeof localStorage !== 'undefined' && localStorage.mmLevel ? parseInt(localStorage.mmLevel) : undefined;
        const initialLevel = queryLevel ?? locallyStoredLevel ?? 0;
        const initialGroup = queryGroup ?? locallyStoredGroup ?? 0;
        this.updateGroupAndLevel(initialGroup, initialLevel)
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
        } else {
        }

        if (!(props.didCheat || props.isSkip)) {
            this.setState({
                celebrate: true,
                lastGameResults: props
            })
        } else {
            this.nextOne(props);
        }
    }

    nextOne(props) {
        const levelShift = props.retreat ? -1 : 1;

        this.updateGroupAndLevel(this.state.currentGroup, (this.state.currentLevel + levelShift + this.state.levels.length) % this.state.levels.length)

    }

    replay() {
        this.updateGroupAndLevel(this.state.currentGroup, this.state.currentLevel);
    }

    setGroup(groupNumber) {
        this.updateGroupAndLevel(groupNumber, 0);
    }

    updateGroupAndLevel(group, level) {

        // Is this valid? If not, fail silently.

        let pool = defaultLevels.filter(x => x.groups.includes(group));
        if (!pool[level]) return false;


        localStorage.mmGroup = group;
        localStorage.mmLevel = level;

        let levels = defaultLevels.filter(x => x.groups.includes(group));

        this.setState({
            celebrate: false, // ALWAYS clear it out
            lastGameResults: null, // Just to avoid any weirdness
            levels: levels,
            currentGroup: group,
            currentLevel: level,
            gameCount: this.state.gameCount + 1
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
                <div className={"maze-controls__group-nav"}>
                    {this.state.groups.filter(x => x.count > 0).map(({name, id, count}) => <div
                        key={id}
                        className={"maze-controls__group"}
                        onClick={() => this.setGroup(id)}>{name} <span className={"number-bubble"}>{count}</span>
                    </div>)}
                </div>
                <div className={"maze-controls__spacer"}/>
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
            {level.description.length && this.state.tab === 'game' && !this.state.celebrate ?
                <p style={{textAlign: 'center'}}>{level.description}</p> : ''}

            {this.state.tab === 'game'
                ? this.state.celebrate
                    ? <Celebrate gameId={this.getCurrentGameId()} key={this.state.gameCount}
                                 results={this.state.lastGameResults} nextLevel={this.nextOne.bind(this)}
                                 replayLevel={this.replay.bind(this)}/>
                    : <><Level key={this.state.gameCount} levelId={level.id} name={level.name}
                               definition={level.definition}
                               inputHandler={this.inputHandler} announceVictory={this.onCurrentLevelWin.bind(this)}/>
                        <Leaderboard hide={true} levelId={level.id} key={'leaderboard-load'}
                                     gameId={this.getCurrentGameId()}/>
                    </>
                : <Leaderboard levelId={level.id} key={this.state.gameCount} gameId={this.getCurrentGameId()}/>

            }
        </div>)
    }

    getCurrentGameId() {
        const level = this.getCurrentLevel();
        return new Board({grid: level.definition}, {}).getInitialHash();
    }
}
