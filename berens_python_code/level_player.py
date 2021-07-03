from puzzle_game1 import *
from more_levels import *
from level_organizer import *

b_try = [[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [1], [4], [101], [4], [1], [], [], [4], [2], [1]], [[1], [4], [], [], [], [1], [], [101], [], [], [1]], [[1], [1], [], [4], [], [1], [], [], [], [], [1]], [[1], [1], [4], [2], [3], [1], [], [], [], [], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_try = Level(b_try, "Let's try!")
print(False == 1)
play_level(l_try)


for i in developing_levels:
    play_level(i)