from puzzle_game1 import *
from more_levels import *
from level_organizer import *

b_try = [[[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [4], [], [], [], []], [[], [], [], [2, 8], [1], [3], [], []], [[], [], [4], [4], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []]]

l_try = Level(b_try, "Let's try!")
play_level(l_try)


for i in experimental_levels:
    play_level(i)
