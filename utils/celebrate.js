import React, {Component} from "react";
import Leaderboard from "../components/leaderboard";
import Board from './logic'
import {toHHMMSS} from "./utils";
import {faRedo} from '@fortawesome/free-solid-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'

const possibleCongrats = [
    'Nice job!',
    'Awesome!',
    'You killed it!',
    'Sweet!',
    'A-maze-ing!',
    'Good show!',
    'Spot on!',


]

export default class Celebrate extends Component {
    constructor(props) {
        super(props);

        this.state = {
            congratulations: possibleCongrats[Math.random() * possibleCongrats.length | 0]
        }
    }

    render() {
        return <div className={"celebrate-wrap"}>
            <div className={"victory-animation"} />
            <div className={"celebrate-header"}>
                <h1>{this.state.congratulations}</h1>
                <h2>Time: {toHHMMSS(this.props.results.runTime)} | Moves: {this.props.results.totalMoves} </h2>
                <div className={"celebrate-buttons"} >
                    <button onClick={()=>this.props.nextLevel(this.props.results)} className={"celebrate-button celebrate-button--next"} >Next Level</button>
                    <button onClick={()=>this.props.replayLevel(this.props.results)} className={"celebrate-button celebrate-button--replay"} ><FontAwesomeIcon icon={faRedo} /></button>
                </div>
            </div>
            <div style={{height: '500px'}} > { /* A wrapper for the leaderboard so it doesn't bounce around */}
                <Leaderboard gameId={this.props.gameId} use={this.props.results} />
                </div>
        </div>
    }
}
