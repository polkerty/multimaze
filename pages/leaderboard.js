import React, {Component} from "react";

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
                timeSince: this.state.since
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

    // https://stackoverflow.com/questions/1322732/convert-seconds-to-hh-mm-ss-with-javascript
    toHHMMSS = (secs) => {
        let sec_num = parseInt(secs, 10)
        let hours = Math.floor(sec_num / 3600)
        let minutes = Math.floor(sec_num / 60) % 60
        let seconds = sec_num % 60

        return [hours, minutes, seconds]
            .map(v => v < 10 ? "0" + v : v)
            .filter((v, i) => v !== "00" || i > 0)
            .join(":")
    }


    render() {
        if (this.state.error) {
            return 'There was an error loading the leaderboard.'
        }
        if (!this.state.ready) return <center>Loading leaderboard...</center>;
        if (!this.state.leaders.length) return <center>Be the first to beat the level!</center>

        return <div className={"leaderboard-wrap"}>
            {this.state.leaders.map(({time, isYou}, index) => {
                return <div className={"leaderboard-entry"}>
                    <span className={"leaderboard-position"}>#{index + 1}</span>
                    <span
                        className={"leaderboard-name " + (isYou ? 'leaderboard-name--me' : '')}>{isYou ? 'Me' : 'Anonymous'}</span>
                    <span className={"leaderboard-time"}>{this.toHHMMSS(time)}</span>
                </div>
            })}
        </div>
        return <pre>{JSON.stringify(this.state.leaders, null, 2)
        }</pre>
    }
}
