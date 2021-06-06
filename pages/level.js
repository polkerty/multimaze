import React, {Component} from "react";

const TOKEN = {
    WALL: 1,
    PLAYER1: 2,
    FINISH1: 3,
    DEATH: 4,
    COLLAPSE: 5,
    BARRIER: 6,
    COIN: 7
}

const CODE_TO_TOKEN = Object.fromEntries(Object.entries(TOKEN).map(([a, b]) => [b, a]));

export default class Level extends Component {
    constructor(props) {
        super(props);
        this.state = {
            board: JSON.parse(JSON.stringify(props.definition))
        }

    }

    render() {
        return <div className={"level-grid"}>
            {
                this.state.board.map(row => (<div className={"level-row"}>
                    {
                        row.map(cell => <Cell def={cell}/>)
                    }
                </div>))
            }
        </div>
    }

}

function Cell(props) {
    return <div className={"level-cell"}>
        {
            props.def.map(code => <div className={"level-token level-token--" + CODE_TO_TOKEN[code]}/>)
        }
    </div>
}
