import React, {Component} from "react";
import {toHHMMSS} from "../utils/utils";

export default class Leaderboard extends Component {
    constructor(props) {
        super(props);

        this.state = {
            leaders: [],
            since: 0,
            ready: false
        }
    }

    componentDidMount() {
        if (typeof window === 'undefined') return;

        fetch(`/api/leaderboard`, {
            method: 'POST',
            body: JSON.stringify({
                gameId: this.props.gameId,
                timeSince: this.state.since,
                use: this.props.use || null
            })
        })
            .then(x => x.json())
            .then(leaders => {
                this.setState({
                    leaders: leaders,
                    ready: true
                })
            }).catch(e => {
            console.error(e);
            this.setState({
                error: true
            })
        })
    }

    render() {
        if (this.state.error) {
            return 'There was an error loading the leaderboard.'
        }
        if (!this.state.ready) return <center>Loading leaderboard...</center>;
        if (!this.state.leaders.length) return <center>Be the first to beat the level!</center>

        return <div className={"leaderboard-wrap"}>
            {this.state.leaders.map(({time, isYou, place}) => {
                return <div className={"leaderboard-entry " + (isYou ? 'leaderboard-entry--me' : '')}>
                    <span className={"leaderboard-position"}>#{place + 1}</span>
                    <span
                        className={"leaderboard-name " + (isYou ? 'leaderboard-name--me' : '')}>{isYou ? 'My best time' : 'Anonymous'}</span>
                    <span className={"leaderboard-time"}>{toHHMMSS(time)}</span>
                </div>
            })}
        </div>
        return <pre>{JSON.stringify(this.state.leaders, null, 2)
        }</pre>
    }
}
