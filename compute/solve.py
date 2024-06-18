# tokens
EMPTY = 0
WALL = 1
PLAYER1 = 2
FINISH1 = 3
DEATH = 4
COLLAPSE = 5
BARRIER = 6
COIN = 7


MAX_ITERS = 100000

def get_neighbors(state, player_squares, coin_count, is_dead):
    n = []
    if is_dead:
        return n
    for m in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        did_state_change, neighbor  = apply(state,player_squares, coin_count, m)
        if did_state_change:
            n.append((m, neighbor))
    return n

def apply(state, player_squares, coin_count, move):
    updates = {}
    new_player_targets = set()
    state_change = False
    for (px, py) in player_squares:
        (tx, ty) = (px + move[0], py + move[1])
        if tx < 0 or ty < 0 or tx > len(state) or ty > len(state[0]):
            # off-world move. Do nothing
            continue

        #### RULES ######
        target = state[tx][ty]

        new_target = []
        can_move_onto = True

        '''
            Previous engines had a concept called "deathbyes" to deal with players temporarily
            sitting on death squares due to the COLLAPSE token. This engine re-write removes
            the concept of a deathbye via the following rule:
            You can *start* a turn on a dead square - but you can't end it there. 
            (This leads to an edge-case nuance in the rules: 
            If someone designs a level with a token on a death square,
            the player does NOT lose if they move immediately off it.)
        '''
        state_change_blocked = False
        for sq in target:
            if DEATH == sq:
                # We don't yet know if we're moving into the square, so we
                # can't return yet here.
                new_target.append(DEATH)
            elif COIN == sq:
                # There is a coin. Assume we can move onto the target, since coins don't co-stack
                # with barriers or walls.
                coin_count -= 1
            elif BARRIER == sq:
                # We're blocked, but the boulder will also be broken.
                can_move_onto = False
            elif COLLAPSE == sq:
                new_target.append(DEATH)
            elif WALL == sq:
                state_change_blocked = True
                can_move_onto = False
                new_target.append(WALL)
            elif FINISH1 == sq:
                new_target.append(FINISH1)
            elif PLAYER1 == sq:
                # We manage players separately. The only reason a player would actually show up here
                # is if this is the original, externally-supplied grid.
                continue

        if not state_change_blocked:
            state_change = True

        new_target = tuple(sorted(target)) # Canonical form
        updates[(tx, ty)] = new_target
    
        # Assign player squares.
        if can_move_onto:
            new_player_targets.add((tx, ty))
        else:
            new_player_targets.add((px, py))

    # Construct next state.
            
    # Another interesting optimization: Since we keep track of player positions
    # entirely separately, we can simply skip storing them in the grid at all,
    # thus avoiding needing to traverse the whole state. 
    
    new_state = list(state)
    for ((x, y), value) in updates.items():
        new_row = list(new_state[x])
        new_row[y] = value
        new_state[x] = tuple(new_row)
    new_state = tuple(new_state)

            
    # Check player squares for death and win conditions. 
    new_player_targets = tuple(sorted(list(new_player_targets)))
    has_won, has_died = check_win_death(new_state, new_player_targets, coin_count)

    return state_change, (new_state, new_player_targets, coin_count, has_won, has_died)

def check_win_death(state, player_squares, coin_count):
    has_won = coin_count == 0
    has_died = False
    for (x, y) in player_squares:
        if DEATH in state[x][y]:
            has_died = True
        if FINISH1 not in state[x][y]:
            has_won = False
    return has_won, has_died


def find_players_and_coins(state):
    players, coins = [], 0
    for i, row in enumerate(state):
        for j, col in enumerate(row):
            if PLAYER1 in col:
                players.append((i, j))
            if COIN in col:
                coins += 1
    return tuple(sorted(players)), coins


from collections import deque
def solve(state, lim=MAX_ITERS):

    # Get information about initial state.
    player_squares, coin_count = find_players_and_coins(state)
    has_won, has_died = check_win_death(state, player_squares, coin_count)

    q = deque([(state, player_squares, coin_count, has_won, has_died, ())]) # Extra tuple is for history.
    iters = 0
    seen = set()

    # TODO: Allow non-optimal wins.
    win, best_win = None, MAX_ITERS

    while len(q) and iters < lim:
        iters += 1

        # print(q[0][-1], q[0][1], q[0][3], q[0][4])
        (state, player_squares, coin_count, has_won, is_dead, history) = q.popleft()

        if (state, player_squares) in seen:
            continue
        seen.add((state, player_squares))
        if has_won:
            return history, iters
        if is_dead:
            continue
        neighbors = get_neighbors(state, player_squares, coin_count, is_dead)
        for m, n in neighbors:
            if (n[0], n[1]) in seen:
                continue
            h = history + (m, )
            q.append(n + (h,))

    return None, iters



    
def print_ans(name, ans):
    (result, iters) = ans
    if not result:
        print(f"{name}: No solution found in {iters} iterations.")
    else:
        for move in result:
            if move == (0, 1):
                print("Right")
            elif move == (1, 0):
                print("Down")
            elif move == (-1, 0):
                print("Up")
            elif move == (0, -1):
                print("Left")
        print(f"{name}: {len(result)} moves - Solved in {iters} iterations.")

def json_to_tuple(grid):
    return tuple(tuple(tuple(cell) for cell in row) for row in grid)

# tests
def test1():
    # Tutorial-8
    grid = [[[1],[1],[1],[1],[1],[1],[1],[1],[1]],[[1],[1],[2],[],[],[],[],[2],[1]],[[1],[1],[1],[5],[1],[1],[1],[1],[1]],[[1],[2],[],[],[],[],[],[1],[1]],[[1],[1],[1],[1],[1],[1],[5],[1],[1]],[[1],[1],[],[],[],[],[],[2],[1]],[[1],[1],[5],[1],[1],[1],[1],[1],[1]],[[1],[2],[],[],[],[],[3],[1],[1]],[[1],[1],[1],[1],[1],[1],[1],[1],[1]]]
    grid = json_to_tuple(grid)
    
    ans = solve(grid)
    print_ans("Tutorial-8", ans)

def test2():
    # Tutorial-8
    grid = [[[1],[1],[1],[1],[1],[1],[1],[1],[1]],[[1],[],[],[],[1],[],[],[],[1]],[[1],[],[1],[],[1],[],[1],[],[1]],[[1],[2],[1],[3],[1],[2],[1],[3],[1]],[[1],[1],[1],[1],[1],[1],[1],[1],[1]],[[1],[],[],[],[1],[],[],[],[1]],[[1],[],[1],[],[1],[],[1],[],[1]],[[1],[2],[1],[3],[1],[2],[1],[3],[1]],[[1],[1],[1],[1],[1],[1],[1],[1],[1]]]
    grid = json_to_tuple(grid)
    
    ans = solve(grid)
    print_ans("Tutorial-1", ans)

def run_all_tests():
    test1()
    # test2()

if __name__ == '__main__':
    run_all_tests()
