from puzzle_game1 import *
from more_levels import *
from level_organizer import *

b_try = [[[1], [], [], [], [], [], [], [4], [2]], [[1], [4], [4], [4], [], [1], [], [], []], [[1], [], [], [], [], [1], [4], [], []], [[1], [], [4], [4], [4], [1], [], [], [1]], [[1], [], [], [], [], [1], [], [], []], [[1], [4], [4], [4], [], [1], [], [9], []], [[1], [2], [], [], [], [1], [1], [], []], [[1], [4, 6], [4, 6], [1], [4, 6], [4, 6], [1], [1], []], [[5], [], [2], [], [3], [], [5], [1], [3]]]
l_try = Level(b_try, "Let's try!")
play_level(l_try)


for i in experimental_levels:
    play_level(i)