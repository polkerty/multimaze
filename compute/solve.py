# tokens
EMPTY = 0
WALL = 1
PLAYER1 = 2
FINISH1 = 3
DEATH = 4
COLLAPSE = 5
BARRIER = 6
COIN = 7


MAX_ITERS = 250000
VERBOSE = False

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
                # Break our rule and look at the entire group
                if not BARRIER in target:
                    new_death_byes.append((tx, ty))
                    new_target.append(DEATH)
                else:
                    new_target.append(COLLAPSE)
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

    initial_state = state
    cleaned_initial_state = clean_state(state)

    # Get information about initial state.
    player_squares, coin_count = find_players_and_coins(state)
    death_byes = ()
    has_won, has_died = check_win_death(state, death_byes, player_squares, coin_count)
    history = ()
    q = deque([(cleaned_initial_state, death_byes, player_squares, coin_count, has_won, has_died, history)])
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
            return history, iters, (time() - now), initial_state
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

    return None, iters, total_time, initial_state



    
def print_ans(name, ans):
    (result, iters, duration, state) = ans
    if not result:
        print(f"{name}: No solution found in {iters} iterations ({duration} secs).")
    else:
        player_squares, coin_count = find_players_and_coins(state)
        death_byes = ()
        has_won, has_died = check_win_death(state, death_byes, player_squares, coin_count)
        print_state(state, death_byes, player_squares, coin_count)
        for move in result:
            did_state_change, (state, death_byes, player_squares, coin_count, has_won, has_died)  = apply(state, death_byes, player_squares, coin_count, move)
                  
            if move == (0, 1):
                print("Right")
            elif move == (1, 0):
                print("Down")
            elif move == (-1, 0):
                print("Up")
            elif move == (0, -1):
                print("Left")
            
            VERBOSE and print_state(state, death_byes, player_squares, coin_count)
        print(f"{name}: {len(result)} moves - Solved in {iters} iterations ({duration} secs).")

def json_to_tuple(grid):
    return tuple(tuple(tuple(cell) for cell in row) for row in grid)

import json
def tuple_to_json(grid):
    lists = list(list(list(cell) for cell in row) for row in grid)
    return json.dumps(lists)

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
    
def test5():
    # Easy-11
    grid = [[[],[5],[],[],[6],[],[7],[1]],[[],[1],[1],[1],[5,6],[4],[],[]],[[],[1],[6],[],[6],[6],[1],[5]],[[],[1],[5],[5],[1],[5,6],[1],[]],[[],[],[],[],[1],[],[],[3]],[[],[1],[1],[1],[1],[1],[4],[]],[[],[1],[3],[],[],[1],[1],[1]],[[2],[1],[2],[],[],[4],[1],[1]]]
    grid = json_to_tuple(grid)
    
    ans = solve(grid)
    print_ans("Easy-11", ans)

def test6():
    # Medium-4
    grid = [[[4],[4],[1],[7],[],[],[],[]],[[],[],[1],[6],[],[],[4],[]],[[2],[],[1],[4],[6],[],[],[4]],[[4],[5],[4],[],[4],[6],[],[]],[[1],[],[4],[],[],[],[],[6]],[[1],[],[4],[],[],[],[6],[]],[[1],[],[4,6],[],[],[6],[4],[]],[[3],[],[4,6],[2],[6],[4],[3],[]]]
    grid = json_to_tuple(grid)
    
    ans = solve(grid)
    print_ans("Medium-4", ans)

def test7():
    # Hard-5
    grid = [[[],[],[],[1],[],[],[3],[1],[5],[5],[5],[5],[5],[5],[3]],[[],[1],[],[1],[],[],[],[1],[5],[5],[5],[5],[5],[5],[5]],[[],[1],[],[1],[],[],[],[1],[5],[5],[5],[5],[5],[5],[5]],[[],[1],[],[1],[1],[1],[],[1],[5],[5],[5],[6],[5],[5],[5]],[[],[1],[],[],[],[],[],[1],[5],[5],[5],[],[5],[5],[5]],[[],[1],[1],[1],[1],[1],[1],[1],[5],[5],[5],[5],[5],[5],[5]],[[2],[],[],[],[],[],[],[1],[2],[5],[5],[5],[5],[5],[5]],[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],[[],[],[],[1],[],[],[3],[1],[6],[6],[6],[6],[6],[6],[3]],[[],[1],[],[1],[],[],[],[1],[6],[6],[6],[6],[6],[6],[6]],[[],[1],[],[1],[],[],[],[1],[6],[6],[6],[6],[6],[6],[6]],[[],[1],[],[1],[1],[1],[],[1],[6],[6],[6],[6],[6],[6],[6]],[[],[1],[],[],[],[1],[],[1],[6],[6],[6],[6],[6],[6],[6]],[[],[1],[1],[1],[1],[1],[],[1],[6],[6],[6],[6],[6],[6],[6]],[[2],[],[],[],[],[],[],[1],[2],[6],[6],[6],[6],[6],[6]]]
    grid = json_to_tuple(grid)
    
    ans = solve(grid)
    print_ans("Hard-5", ans)

def run_all_tests():
    # test1()
    # test2()
    # test3()
    test4()
    # test5()
    # test6()
    # test7()

if __name__ == '__main__':
    run_all_tests()

######### HILL CLIMBING #############
from random import randrange, choices
POSSIBLE_VALUES = [
    [EMPTY],
    [WALL],
    [PLAYER1],
    [FINISH1],
    [DEATH],
    [COLLAPSE],
    [BARRIER],
    [COIN],
    [COLLAPSE, BARRIER],
    [DEATH, BARRIER],
    [COLLAPSE, COIN],
    [FINISH1, COIN],
    [FINISH1, BARRIER]   
]

WEIGHTS = (
    4,
    10,
    1,
    1,
    2,
    3,
    1,
    2,
    4,
    1,
    1,
    1,
    1,
)
def mutate_grid(grid, change_cnt, max_deg_of_freedom, max_tries=300):
    tries = 0
    original_players = count_players(grid)
    while tries < max_tries:
        tries += 1
        mutable_grid = list(list(list(cell) for cell in row) for row in grid)
        for _ in range(change_cnt):
            row_pos = randrange(0, len(mutable_grid))
            col_pos = randrange(0, len(mutable_grid[0]))
            mutable_grid[row_pos][col_pos] = choices(POSSIBLE_VALUES, weights=WEIGHTS, k=1)[0]
        if count_players(mutable_grid) != original_players:
            continue 
        if count_degrees_of_freedom(mutable_grid) <= max_deg_of_freedom:
            break
    return json_to_tuple(mutable_grid)


def score(path):
    if not path:
        return 0
    last = None
    val = 0
    for item in path:
        if item != last:
            last = item
            val += 1
    return val

def count_degrees_of_freedom(grid):
    tot = 0
    for row in grid:
        for col in row:
            if any(token in (COLLAPSE, COIN, BARRIER) for token in col):
                tot += 1
    return tot

def count_players(grid):
    tot = 0
    for row in grid:
        for col in row:
            if PLAYER1 in col:
                tot += 1
    return tot

##### MODAL ######
# I can't figure out how to import stuff from other files
# and make it work for Modal,
# so it'll all just have to go here for now.
    
import modal
stub = modal.App("multimaze-searcher")


@stub.function()
def hillclimb(x, change_cnt, max_deg_of_freedom):
    x = json_to_tuple(x)
    x2 = mutate_grid(x, change_cnt, max_deg_of_freedom)
    result = solve(x2)
    return x2, result

@stub.function()
def solve_grid(x):
    x = json_to_tuple(x)
    result = solve(x)
    return result


@stub.local_entrypoint()
def main():
    # grid = [[[1],[1],[1],[1],[1],[1],[1],[1],[1]],[[1],[1],[2],[],[],[],[],[2],[1]],[[1],[1],[1],[5],[1],[1],[1],[1],[1]],[[1],[2],[],[],[],[],[],[1],[1]],[[1],[1],[1],[1],[1],[1],[5],[1],[1]],[[1],[1],[],[],[],[],[],[2],[1]],[[1],[1],[5],[1],[1],[1],[1],[1],[1]],[[1],[2],[],[],[],[],[3],[1],[1]],[[1],[1],[1],[1],[1],[1],[1],[1],[1]]]
    # Mostly empty 6x11 grid, in the spirit of the old curated puzzles.
    grid = [[[],[],[],[3],[1],[],[],[],[3]],[[],[],[],[],[1],[],[],[],[]],[[],[],[],[],[1],[],[],[],[]],[[2],[],[],[],[1],[2],[],[],[]]]    
    baseline = solve_grid.remote(grid)
    (b_result, b_iters, b_duration, b_state) = baseline

    if not b_result:
        raise ValueError("Initial grid is not solveable")
    
    print("Baseline difficulty: ", score(b_result), b_iters)

    best, difficulty, prev_iter_cap = (grid, baseline), score(b_result), b_iters
    for (parallel, mutation_count, min_iters, max_iters, max_deg_freedom) in [
        (999, 9, 0, 120000, 3),
        (999, 4, 0, 160000, 4),
        (999, 3, 0, 250000, 6),
    ]:
        trials = hillclimb.starmap([
            (grid, mutation_count, max_deg_freedom) for _ in range(parallel)
        ])
        
        for ans in trials:
            grid, (result, iters, duration, state) = ans
            s = score(result)
            # print('\t', s, len(result) if result else 'x', iters, count_degrees_of_freedom(grid))
            if result and (s > difficulty or (s == difficulty and iters < prev_iter_cap)) \
                and iters < max_iters and iters > min_iters and \
                count_degrees_of_freedom(grid) <= max_deg_freedom and count_players(grid) == 2: # and \
                # iters < prev_iter_cap * (1.1**(len(result) - difficulty)):
                 # The computer's number of moves to solve it should increase by no more than 5% \
                # for each additional step of difficulty. \
                best, difficulty, prev_iter_cap = (grid, ans), s, iters

        if not best:
            print("No improvements were found.")
        else:
            print(best[1])
            print(difficulty, prev_iter_cap, count_degrees_of_freedom(best[0]))
            print(tuple_to_json(best[0]))



    
