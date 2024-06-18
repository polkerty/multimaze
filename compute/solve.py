# tokens
EMPTY = 0
WALL = 1
PLAYER1 = 2
FINISH1 = 3
DEATH = 4
COLLAPSE = 5
BARRIER = 6
COIN = 7


MAX_ITERS = 1000000

def print_state(state, death_byes, player_squares, coin_count):
    for r in state:
        print(r)
    print('Death byes: ', death_byes)
    print('Players: ', player_squares)
    print('Coins: ', coin_count)

def get_neighbors(state, death_byes, player_squares, coin_count, is_dead):
    n = []
    if is_dead:
        return n
    for m in ((-1, 0),(1, 0),(0, -1),(0, 1)):
        did_state_change, (new_state, new_death_byes, new_player_targets, coin_count, has_won, has_died)  = apply(state, death_byes, player_squares, coin_count, m)
        if did_state_change and not has_died:
            n.append((m, (new_state, new_death_byes, new_player_targets, coin_count, has_won, has_died)))
    return n

# Note: DEATH_BYES are a very nuanced field. We pass them around
# everywhere, but mostly for memoization reasons, as the logic
# they encapsulate is checked immediately after they are generated,
# entirely within this function.
# Nevertheless, we want to return the death_byes from the function because they represent 
# state, which we use in the memoization of the solver function,
# and we even pass in the *previous* death_byes to this function to help us understand
# if that demonstrates this pass will not be a no-op, even if the contents
# of the grid do not change.
def apply(state, death_byes, player_squares, coin_count, move):
    updates = {}
    new_player_targets = set()
    new_death_byes = []

    # If the previous step generated a death bye, that guarantees 
    # that THIS step would invalidate it, so it will not be a no-op.
    # (But there are many other ways for this to not be a no-op.)
    is_mutating_op = len(death_byes) > 0
    for (px, py) in player_squares:
        (tx, ty) = (px + move[0], py + move[1])
        if tx < 0 or ty < 0 or tx >= len(state) or ty >= len(state[0]):
            # off-world move. Do nothing
            new_player_targets.add((px, py))
            continue

        #### RULES ######
        target = tuple(sorted(state[tx][ty]))

        new_target = []
        can_move_onto = True

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
                new_death_byes.append((tx, ty))
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
            is_mutating_op = True

        new_target = tuple(sorted(new_target)) # Canonical form
        if target != new_target:
            updates[(tx, ty)] = new_target
    
        # Assign player squares.
        if can_move_onto:
            new_player_targets.add((tx, ty))
        else:
            new_player_targets.add((px, py))

    new_death_byes = tuple(sorted(new_death_byes))
    if not is_mutating_op:
        # Assume no win/loss, since we wouldn't be attempting a move if we had.
        # Since we had no mutations, save the trouble of copying state (below).
        return is_mutating_op, (state, new_death_byes, player_squares, coin_count, False, False)

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
    # Note that the new death_byes are used here.
    has_won, has_died = check_win_death(new_state, new_death_byes, new_player_targets, coin_count)

    return is_mutating_op, (new_state, new_death_byes, new_player_targets, coin_count, has_won, has_died)

def check_win_death(state, death_byes, player_squares, coin_count):
    has_won = coin_count == 0
    has_died = False
    for (x, y) in player_squares:
        if DEATH in state[x][y] and (x, y) not in death_byes:
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

def clean_state(state):
    return tuple(
        tuple(
            tuple(sorted(list(t for t in cell if t != PLAYER1)))
            for cell in row
        )
        for row in state
    )

from collections import deque
from time import time
def solve(state, lim=MAX_ITERS):
    now = time()

    # Get information about initial state.
    player_squares, coin_count = find_players_and_coins(state)
    death_byes = ()
    has_won, has_died = check_win_death(state, death_byes, player_squares, coin_count)
    history = ()
    q = deque([(clean_state(state), death_byes, player_squares, coin_count, has_won, has_died, history)])
    iters = 0
    generated = set()


    # TODO: Allow non-optimal wins.
    win, best_win = None, MAX_ITERS

    while len(q) and iters < lim:
        iters += 1

        (state, death_byes, player_squares, coin_count, has_won, is_dead, history) = q.popleft()

        # This log message can be useful when comparing two different solvers.
        # print(', '.join(', '.join(str(t) for t in x) for x in history))

        if has_won:
            for r in state:
                print(r)
            print(death_byes)
            print(player_squares)
            print(coin_count)
            print(is_dead)
            return history, iters, (time() - now)
        if is_dead:
            continue
        neighbors = get_neighbors(state, death_byes, player_squares, coin_count, is_dead)

        for m, n in neighbors:
            if (n[0], n[1], n[2]) in generated:
                continue
            generated.add((n[0], n[1], n[2]))

            h = history + (m, )
            q.append(n + (h,))

    total_time = time() - now

    return None, iters, total_time



    
def print_ans(name, ans):
    (result, iters, duration) = ans
    if not result:
        print(f"{name}: No solution found in {iters} iterations ({duration} secs).")
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
        print(f"{name}: {len(result)} moves - Solved in {iters} iterations ({duration} secs).")

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
    # Tutorial-1
    grid = [[[1],[1],[1],[1],[1],[1],[1],[1],[1]],[[1],[],[],[],[1],[],[],[],[1]],[[1],[],[1],[],[1],[],[1],[],[1]],[[1],[2],[1],[3],[1],[2],[1],[3],[1]],[[1],[1],[1],[1],[1],[1],[1],[1],[1]],[[1],[],[],[],[1],[],[],[],[1]],[[1],[],[1],[],[1],[],[1],[],[1]],[[1],[2],[1],[3],[1],[2],[1],[3],[1]],[[1],[1],[1],[1],[1],[1],[1],[1],[1]]]
    grid = json_to_tuple(grid)
    
    ans = solve(grid)
    print_ans("Tutorial-1", ans)

def test3():
    # Tutorial-7
    grid = [[[1],[1],[1],[1],[1],[1],[1],[1]],[[1],[2,3],[1],[7],[7],[1],[2,3],[1]],[[1],[1],[4],[],[],[4],[1],[1]],[[1],[3],[],[5],[5],[],[7],[1]],[[1],[2,3],[],[5],[5],[],[7],[1]],[[1],[1],[4],[],[],[4],[1],[1]],[[1],[2,3],[1],[7],[7],[1],[2,3],[1]],[[1],[1],[1],[1],[1],[1],[1],[1]]]
    grid = json_to_tuple(grid)
    
    ans = solve(grid)
    print_ans("Tutorial-7", ans)
    
def test4():
    # Tutorial-10
    grid = [[[1],[1],[1],[1],[1],[1],[1],[1]],[[1],[1],[1],[5],[3],[5],[1],[1]],[[1],[1],[5],[5],[5],[5],[5],[1]],[[],[],[5],[5],[5],[5],[5],[1]],[[2],[],[5],[5],[5],[5],[5],[7]],[[1],[1],[5,6],[5,6],[5,6],[5,6],[5,6],[]],[[1],[1],[],[],[],[],[],[]],[[1],[1],[1],[1],[1],[1],[1],[1]]]
    grid = json_to_tuple(grid)
    
    ans = solve(grid)
    print_ans("Tutorial-10", ans)

def run_all_tests():
    # test1()
    # test2()
    # test3()
    test4()

if __name__ == '__main__':
    run_all_tests()
