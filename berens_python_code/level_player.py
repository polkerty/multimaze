from puzzle_game1 import *
from more_levels import *
from level_organizer import *

b_try = [[[1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [4], [2], [], [1], [9], [1], [], [1]], [[1], [], [], [], [1], [], [3], [], [1]], [[1], [], [1], [3], [1], [5], [2], [], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_try = Level(b_try, "Let's try!")


for i in developing_levels:
    play_level(i)