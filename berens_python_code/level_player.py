from puzzle_game1 import *
from more_levels import *
from level_organizer import *

b_try = [[[1], [1], [1], [1], [1], [], [], []], [[1], [1], [1], [1], [], [], [4], [3]], [[1], [1], [7], [], [], [1], [1], []], [[1], [], [4], [], [], [], [], []], [[2], [], [1], [1], [1], [1], [], [5, 6]], [[1], [], [], [], [], [], [], []], [[1], [1], [1], [1], [1], [4], [1], [4]], [[1], [1], [1], [1], [4, 6], [], [3], [2]]]
l_try = Level(b_try, "Let's try!")
play_level(l_cubic)


for i in experimental_levels:
    play_level(i)