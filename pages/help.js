import {Cell, TOKEN} from "./level";
import {faTimes} from '@fortawesome/free-solid-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'

export default function Help(props) {
    return <div className={"help-modal__wrap"}>
        <div className={"help-modal__inner"}>
            <div className={"help-modal__close"} onClick={() => props.closeHelp()}>
                <FontAwesomeIcon icon={faTimes}/>
            </div>
            <div className={"help-modal__content"}>
                <ul>
                    <li>The object of the game is to move your players <Cell def={[TOKEN.PLAYER1]} size={30}/> to first
                        collect all the coins <Cell def={[TOKEN.COIN]} size={30}/> and then simultaneously land on the
                        victory squares
                        <Cell def={[TOKEN.FINISH1]} size={30}/>.
                    </li>
                    <li>You can move your players left, right, up, or down together by using the arrow keys or WASD.
                    </li>
                    <li>But you're blocked from moving on to the walls <Cell def={[TOKEN.WALL]} size={30}/>, and
                        if you move onto the death squares
                        <Cell def={[TOKEN.DEATH]} size={30}/> you lose. These squares <Cell def={[TOKEN.COLLAPSE]}
                                                                                            size={30}/> turn into death
                        squares after you've landed on them once. Also watch out for barrier cells <Cell def={[TOKEN.BARRIER]}
                                                                                                         size={30}/>. It takes an extra turn to destroy
                        the barrier before you can move onto the cell.
                    </li>
                    <li>Once you defeat a level, you'll automatically move up to the next one. Good luck!</li>
                </ul>
            </div>
        </div>
    </div>
}
