from puzzle_game1 import *
from more_levels import *
"""
REGISTRY OF ALL LEVELS

Experimental:
l_exp1 : Parity level, needs a bit of work to make only one door level
l_exp2 : Simple cycling level, could be revised to look nicer

Tutorial:
l_tut1 : Learning how the game works (three doing same path)
l_tut2 : learning about lava
l_tut3 : having to get on finish at same time
l_tut4 : coins
l_tut5 : boulders
l_tutorange : NEW orange tutorial
l_tut6 : merging
l-------------------- _tut7 : orange :Turned to easy
-----------------l_tut8 : replaced by below
l_boulderlava2: too easy for medium, so replaced here
l_tut9 : old merge level, not currently in use
l_tut10 : boulders on orange
l_tut11 : impossible

Easy: 
-------------------l_real : simple level with two little mazes (OBSOLETE)
l_maze_pair : simple level that is two mazes interposed
------------------l_single : be careful with the orange! (OBSOLTETE, IN TUTORIAL)
l_boulders1 : just use boulders carefully
l_backforth : fun one, simple parity thing
 ---------------- l_clearing : use the open square well (SCRAPPED)
l_ok : nothing fancy here, but multiple plausible options
l_orangeline : spacing right
l_tutfinale : chaned into easy finale


Medium:
l_oneway : interesting one way doors simulated
l_climb : climbing to the coin
l_tacking : one player stuck in a red square, be careful to get out
l_backtrack : fun requirement of backtracking
l_merge : tricky merging required, but currently not as hard as it could be
l_asy : cute level using orange


Hard:
l_climb2 : clever variant on climb
l_boulders2: tricky orange on boulders
L_statisfying: nice parity thing, clever
l_satisfying2: nice variant of above
l_satisfying3: yet another variant!
l_satisfying4: currently bad, needs work
l_thin_ice : lots of orange in one area
l_mediocre : not really well designed, some spirals
l_rip : not well designed, needs to be better thought out, not even that hard?


Discarded:
l_intro2 : This was the or

Development:
l_zagswitch
"""

ALL = 0
EASY = 1
MEDIUM = 2
HARD = 3
CLASSIC = 4
TUTORIAL = 5
EXPERIMENTAL = 6
RANDOM = 7
CURATED = 8
def set_difficulty(arr, difficulty):
    for i in arr:
        i.set_group([difficulty])

#randomness
with open('random_multimaze_collection_2.txt', 'r') as file:
    data = file.read().replace('\n', '')
random_bunch = eval(data)

#development
with open('random_multimaze_collection_3.txt', 'r') as file:
    data2 = file.read().replace('\n', '')
random_flip_bunch = eval(data2)

random_levels = []
par = [39, 47, 33, 31, 48, 40, 36, 34, 34, 35, 51, 39, 31, 33, 32, 33, 34, 31, 33, 37, 36, 32, 37, 46, 24, 24, 22, 25, 23, 25, 24, 24, 29, 22, 30, 22, 27, 23, 28, 24, 22, 27, 25, 23, 23, 23, 25, 23, 29, 64, 82, 68, 74, 101, 42, 44, 60, 43, 53, 56, 72, 59, 69, 63, 53, 59, 43, 26, 22, 27, 23, 27, 28, 22, 25, 22, 31, 25, 22, 28, 30, 34, 25, 26, 27, 22, 27, 22, 27, 25, 31, 24, 23, 35, 35]
for i in range(len(random_bunch)):
    if i == 0:
        random_levels.append(Level(random_bunch[i], "Random", "Thanks to Drake Thomas for random generation!"))
    else:
        random_levels.append(Level(random_bunch[i], "Random"))

random_flip_levels = []
for i in range(len(random_flip_bunch)):
        random_flip_levels.append(Level(random_flip_bunch[i], "Time to fail"))

tutorial_levels = [l_tut1, l_tut2, l_tut3, l_tutfinishes, l_tut4, l_tut5, l_tutorange, l_tutmerge, l_tut8, l_tut10, l_tut11]
easy_levels = [l_figureeight, l_maze_pair, l_boulders1, l_backforth, l_easyorange, l_ok, l_orangeline, l_oneway]
medium_levels = [l_tacking, l_constrained, l_climb, l_easymerge, l_tutfinale, l_backtrack, l_merge, l_asym]
hard_levels = [l_climb2, l_satisfying, l_boulders2, l_satisfying2, l_thin_ice, l_satisfying3, l_mediocre, l_rip]
experimental_levels = [l_exp1, l_exp2, l_thin, l_thin2] + [l_zagswitch, l_helpkey, l_swapmaze] + [l_cubic, l_number, l_clever]
developing_levels = [l_zagswitch, l_helpkey, l_swapmaze] + random_flip_levels
curated_levels = [l_hardgood, l_glorious]
all_levels = tutorial_levels + easy_levels + medium_levels + hard_levels + experimental_levels + curated_levels + random_levels



set_difficulty(tutorial_levels, TUTORIAL)
set_difficulty(easy_levels, EASY)
set_difficulty(medium_levels, MEDIUM)
set_difficulty(hard_levels, HARD)
set_difficulty(experimental_levels, EXPERIMENTAL)
set_difficulty(random_levels, RANDOM)
set_difficulty(curated_levels, CURATED)
#set_difficulty(developing_levels, DEVELOPING)

make_json(all_levels)

        