from puzzle_game1 import *
#ALL EASY MEDIUM HARD CLASSIC TUTORIAL RANDOM


b_clever = [[[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]], [[4], [], [], [106], [103], [], [], [104], [], [], [4]], [[4], [2], [100], [], [105], [108], [101], [], [], [3], [4]], [[4], [2], [], [103], [], [109], [], [102], [], [3], [4]], [[4], [2], [101], [], [100], [], [], [], [], [3], [4]], [[4], [], [102], [], [], [105], [], [108], [109], [], [4]], [[4], [], [], [], [104], [], [], [106], 
[], [], [4]], [[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]]]
l_clever = Level(b_clever, "Easier than it seems", "Though that isn't saying much, is it?")

b_number = [[[4], [100], [], [], [3], [], [], [], [], [3], [], [], [100], [4]], [[4], [], [], [], [], [], [], [], [], [], [], [], [], [4]], [[4], [], [], [], [], [], [], [], [], [], [], [], [], [4]], [[4], [], [], [], [], [], [], [], [], [], [], [], [], [4]], [[4], [2], [], [], [], [], [], [], [], [], [], [2], [], [4]], [[4], [], [], [], [], [], [], [], [], [], [], [], [], [4]], [[4], [], [], [], [], [], [], [], [], [], [], [], [], [4]], [[4], [101], [], [], [], [], [], [], [], [], [], [101], [4], [4]]]
l_number = Level(b_number, "Math Time!")

b_cubic = [[[4], [103], [1], [3], [], [1], [1], [4]], [[1], [2], [4], [1], [2], [], [1], [3, 2]], [[4], [], [4], [1], [1], [], [], [1]], [[4], [3], [4], [105], [], [1], [], []], [[4], [], [4], [1], [], [], [1], [105]], [[4], [], [4], [1], [1], [], [], [1]], [[4], [], [4], [1], [1], [1], [], []], [[4], [103], [4], [3], [2, 3], [4], [1], [9]]]
l_cubic = Level(b_cubic, "Tedium", "More interesting in theory than in practice")
#After this, we had levels to top
b_intro2 = [[[1], [], [], [], [], [], [7], []], [[1], [], [], [], [], [1], [1], [1]], [[1], [], [], [], [], [1], [1], [1]], [[1], [5], [4], [5], [4], [1], [1], [1]], [[1], [5], [4], [5], [4], [1], [1], [1]], [[], [], [], [], [], [6], [], []], [[], [2], [], [], [], [6], [], [3]], [[], [], [], [], [], [6], [], []]]
l_intro2 = Level(b_intro2, "Intro", "This was the only tutorial originally", groups = [0,4,1])

b_real =\
[[[3],[1],[1],[0],[1],[0]],
 [[0],[0],[1],[0],[0],[0]],
 [[1],[0],[1],[2],[1],[0]],
 [[2],[0],[1],[1],[3],[0]]]
l_real = Level(b_real, "Simple", groups = [0,1,4])

b_tacking = [[[], [], [], [], [1], [], [], [], [], [1]], [[3], [], [1], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [1], [], []], [[1], [], [], [], [1], [], [], [], [], []], [[4], [4], [4], [4], [4], [4], [], [], [], []], [[4], [], [], [], [], [4], [], [], [], [1]], [[4], [], [2], [], [], [4], [], [1], [], []], [[4], [], [], [3], [], [4], [], [], [], []], [[4], [], [], [], [], [4], [], [], [], []], [[4], [4], [4], [4], [4], [4], [], [2], [1], []]]
l_tacking = Level(b_tacking, "Tacking", grid_size = 80, groups = [0,4,2])

b_backtrack = [[[], [], [4], [1], [1], [1], [1], [1], [1], [], [], [], [], [], [], [], [3]], [[], [], [], [], [], [], [], [], [1], [], [1], [4], [1], [], [], [], []], [[], [4], [4], [4], [4], [], [], [], [1], [], [4], [4], [4], [1], [4], [], []], [[], [], [], [], [], [], [1], [], [1], [], [], [], [], [], [], [4], []], [[4], [4], [1], [4], [], [4], [4], [4], [1], [4], [4], [4], [], [4], [4], [1], [1]], [[], [], [], [], [], [], [], [], [1], [1], [], [], [], [], [], [], []], [[1], [4], [4], [4], [4], [4], [], [4], [1], [4], [4], [4], [4], [4], [4], [], [4]], [[], [2], [], [], [], [], [], [3], [1], [], [2], [], [], [], [], [], []]]
l_backtrack = Level(b_backtrack, "Backtrack", groups = [0,4,2], grid_size = 80)

b_constrained = [[[], [1], [1], [1], [], [], [4], [], [], [], [], [1], [], [], [], [], []], [[3], [1], [], [], [], [], [4], [], [], [1], [], [1], [], [1], [], [], [1]], [[], [1], [1], [4], [4], [], [4], [], [1], [1], 
[], [1], [], [1], [], [], []], [[5], [1], [4], [], [], [], [4], [], [], [1], [], [1], [], [1], [1], [4], []], [[], [1], [], [], [4], [], [], [], [], [1], [], [], [], [1], [], [], []], [[], [1], [], [1], [4], [], [4], [1], [], [1], [1], [1], [1], [], [], [], [3]], [[], [1], [], [], [], [], [], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]], [[2], [1], [2], [], [], [], [], [1], [2], [], [], [], [], [5], [5], [], [3]]]
l_constrained = Level(b_constrained, "Constrained", groups = [0,4,2], grid_size = 80)

b_thin_ice = [[[], [], [], [1], [], [], [3], [1], [5], [5], [5], [5], [5], [5], [3]], [[], [1], [], [1], [], [], [], [1], [5], [5], [5], [5], [5], [5], [5]], [[], [1], [], [1], [], [], [], [1], [5], [5], [5], [5], 
[5], [5], [5]], [[], [1], [], [1], [1], [1], [], [1], [5], [5], [5], [6], [5], [5], [5]], [[], [1], [], [], [], [], [], [1], [5], [5], [5], [], [5], [5], [5]], [[], [1], [1], [1], [1], [1], [1], [1], [5], [5], [5], [5], [5], [5], [5]], [[2], [], [], [], [], [], [], [1], [2], [5], [5], [5], [5], [5], [5]], [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]], [[], [], [], [1], 
[], [], [3], [1], [6], [6], [6], [6], [6], [6], [3]], [[], [1], [], [1], [], [], [], [1], [6], [6], [6], [6], [6], [6], [6]], [[], [1], [], [1], [], [], [], [1], [6], [6], [6], [6], [6], [6], [6]], [[], [1], [], [1], [1], [1], [], [1], [6], [6], [6], [6], [6], [6], [6]], [[], [1], [], [], [], [1], [], [1], [6], [6], [6], [6], [6], [6], [6]], [[], [1], [1], [1], [1], [1], [], [1], [6], [6], [6], [6], [6], [6], [6]], [[2], [], [], [], [], [], [], [1], [2], [6], [6], [6], [6], [6], [6]]]
l_thin_ice = Level(b_thin_ice, "Thin Ice", "Be thankful for what you're given", groups = [0,4,2], grid_size = 50)

b_mediocre = [[[], [], [], [], [], [3], [], [], [1], [], [], [], [], [], [], [], []], [[], [4, 6], [4, 6], [4, 6], [4, 6], [4, 6], [4, 6], [], [1], [], [4, 6], [4, 6], [4, 6], [4, 6], [4, 6], [4, 6], []], [[], [4, 
6], [], [], [], [], [], [], [1], [], [4, 6], [], [], [], [], [4, 6], []], [[], [4, 6], [], [4, 6], [4, 6], [4, 6], [], [], [1], [], [4, 6], [], [4, 6], [4, 6], [], [4, 6], []], [[], [4, 6], [], [4, 6], [], [], [], [], [1], [], [4, 6], [], [4, 6], [], [3], [4, 6], []], [[], [], [], [], [], [4, 6], [], [4, 6], [1], [], [4, 6], [], [4, 6], [], [], [4, 6], []], [[], [4, 6], [], [4, 6], [4, 6], [4, 6], [], [4, 6], [1], [], [4, 6], [], [4, 6], [4, 6], [4, 6], [4, 6], []], [[2], [4, 6], [], [], [], [], [], [4, 6], [1], [2], [4, 6], [], [], [], [], [], []]]
l_mediocre = Level(b_mediocre, "Mediocre", "Not actually a good level", groups = [0,4,3], grid_size = 80)

b_single = [[[1], [1], [], [3], [], [1]], [[1], [1], [5], [5], [5], [1]], [[1], [1], [5], [5], [5], [1]], [[2], [], [5], [5], [5], [7]], [[1], [1], [5, 6], [5, 6], [5, 6], []], [[1], [1], [], [], [], []]]
l_single = Level(b_single, "Single", "Still learning the ropes", groups = [0,4,1])

b_maze_pair = [[[], [], [], [], [], [], [3], [1], [], [], [], [], [7, 7, 7, 7, 7, 7], [4], [3]], [[], [1], [4], [1], [4], [1], [], [1], [], [1], [], [1], [], [1], []], [[], [], [], [], [], [], [], [1], [], [], [], [4], [], [], []], [[], [1], [], [1], [], [1], [4], [1], [], [1], [], [1], [], [1], []], [[], [], [], [], [], [], [], [1], [], [4], [], [], [], [4], []], [[], [1], [4], [1], [4], [1], [], [1], [], [1], [], [1], [], [1], []], [[2], [], [], [], [], [], [], [1], [2], [], [], [], [], [], []]]
l_maze_pair = Level(b_maze_pair, "Maze Pair", "Some have found crossing their eyes to be effective here", groups = [0,4,1], grid_size = 100)

b_oneway = [[[], [5], [], [], [6], [], [7], [1]], [[], [1], [1], [1], [5, 6], [4], [], []], [[], [1], [6], [], [6], [6], [1], [5]], [[], [1], [5], [5], [1], [5, 6], [1], []], [[], [], [], [], [1], [], [], [3]], [[], [1], [1], [1], [1], [1], [1, 4], []], [[], [1], [3], [], [], [1], [1], [1]], [[2], [1], [2], [], [], [4], [1], [1]]]
l_oneway = Level(b_oneway, "Oneway", "The last easy level: good luck!", groups = [0,4,2], grid_size = 100)

b_climb = [[[4], [4], [1], [7], [], [], [], []], [[], [], [1], [6], [], [], [4], []], [[2], [], [1], [4], [6], [], [], [4]], [[4], [5], [4], [], [4], [6], [], []], [[1], [], [4], [], [], [], [], [6]], [[1], [], [4], [], [], [], [6], []], [[1], [], [4, 6], [], [], [6], [4], []], [[3], [], [4, 6], [2], [6], [4], [3], []]]
l_climb = Level(b_climb, "Climb", "Climb to the coin!", groups = [0,4,2], grid_size = 100)

b_climb2 = [[[4], [4], [1], [7], [], [], [], []], [[], [], [1], [6], [], [], [4], []], [[2], [], [1], [4], [6], [], [], [4]], [[4], [5], [4], [], [4], [6], [], []], [[1], [], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [], [], [], [], []], [[1], [], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [], [], [], [], []], [[1], [], [4, 6], [], [], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [4], []], [[3], [], [4, 6], [2], [], [], [3], []]]
l_climb2 = Level(b_climb2,"Climb2", "Climb to the coin!", groups = [0,4,3], grid_size = 100)

b_boulders1 = [[[4], [4], [4], [1], [4], [4], [4], [1], [4], [4], [4], [4], [4], [4], [4], [4], [4]], [[], [], [], [1], [], [], [], [1], [4], [], [], [], [], [], [], [], [4]], [[], [1], [], [1], [], [1], [], [1], [4], [], [], [], [], [], [3], [], [4]], [[], [1], [], [1], [], [1], [], [1], [4], [6], [6], [6], [6], [6], [6], [6], [4]], [[], [1], [], [1], [], [1], [], [1], [4], [6], [6], [6], [6], [6], [6], [6], [4]], [[], [1], [], [1], [], [1], [3], [1], [4], [], [2], [], [], [], [], [], [4]], [[2], [1], [], [], [], [1], [], [1], [4], [], [], [], [], [], [], [], [4]], [[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]]]
l_boulders1 = Level(b_boulders1, "Boulders 1", groups = [0,4,1], grid_size = 80)

b_boulders2 = [[[4], [4], [4], [4], [4], [4], [4], [1], [4], [4], [4], [4], [4], [4], [4], [4], [4]], [[], [], [], [4], [], [], [], [1], [4], [], [], [], [], [], [], [], [4]], [[], [1], [], [4], [], [1], [], [1], [4], [], [], [], [], [], [3], [], [4]], [[], [1], [], [4], [], [1], [], [1], [4], [6], [6, 5], [6], [6, 5], [6], [6, 5], [6], [4]], [[], [1], [], [4], [], [1], [], [1], [4], [6, 5], [6], [6, 5], [6], [6, 5], [6], [6, 5], [4]], [[], [1], [], [4], [], [1], [3], [1], [4], [], [2], [], [], [], [], [], [4]], [[2], [1], [], [], [], [1], [], [1], [4], [], [], [], [], [], [], [], [4]], [[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]]]
l_boulders2 = Level(b_boulders2, "Boulders 2", groups = [0,4,3], grid_size = 80)

b_satisfying = [[[4], [4], [4], [4], [4], [4], [4], [4], [4], [4, 6], [4]], [[4], [7], [], [3], [4], [3], [], [], [], [6], [4]], [[4], [], [1], [], [1], [5], [1], [], [1], [], [4]], [[4], [], [5], [], [], [], [4], [], [], [], [4]], [[4], [], [1], [], [1], [5], [1], [], [4], [], [4]], [[4], [], [], [], [5], [], [], [], [], [], [4]], [[4], [], [1], [], [1], [], [1], [4], [1], [5], [4]], [[4], [], [4], [2], [], [], [], [], [], [], [4]], [[4], [], [1], [4], [1], [4], [1], [5], [1], [], [4]], [[4, 6], [2], [], [], [], [], [], [], [], [], [4]], [[4], [4, 6], [4], [4], [4], [4], [4], [4], [4], [4], [4]]]
l_satisfying = Level(b_satisfying, "Have Fun", "This is a good level", groups = [0,4,3], grid_size = 70)

b_satisfying2 = [[[4], [4], [4], [4], [4], [4], [4], [4], [4], [4, 6], [4]], [[4], [7], [], [], [4], [3], [], [], [], [6], [4]], [[4], [], [1], [], [1], [5], [1], [], [4], [], [4]], [[4], [], [5], [3], [], [], [4], [], [], [], [4]], [[4], [], [1], [], [1], [5], [4], [], [4], [], [4]], [[4], [], [], [], [5], [], [], [], [], [], [4]], [[4], [], [4], [], [4], [], [4], [4], [1], [5], [4]], [[4], [], [4], [2], [], [], [], [], [], [], [4]], [[4], [], [1], [4], [1], [4], [1], [5], [1], [], [4]], [[4, 6], [2], [], [], [], [], [], [], [], [], [4]], [[4], [4, 6], [4], [4], [4], [4], [4], [4], [4], [4], [4]]]
l_satisfying2 = Level(b_satisfying2, "Have Fun 2", groups = [0,4,3], grid_size = 70)

b_satisfying3 = [[[4], [4], [4], [4], [4], [4], [4], [4], [4], [4, 6], [4]], [[4], [7], [], [], [4], [3], [], [], [], [6], [4]], [[4], [], [1], [], [1], [5], [1], [], [4], [], [4]], [[4], [], [5], [3], [], [], [4], [], [], [], [4]], [[4], [], [1], [], [1], [5], [4], [], [1], [], [4]], [[4], [], [], [], [5], [], [], [], [], [], [4]], [[4], [], [1], [], [4], [], [4], [4], [1], [5], [4]], [[4], [], [4], [2], [], [], [], [], [], [], [4]], [[4], [], [1], [4], [1], [4], [1], [5], [1], [], [4]], [[4], [2], [], [], [], [], [], [], [], [], [4]], [[4], [4, 6], [4], [4], [4], [4], [4], [4], [4], [4], [4]]]
l_satisfying3 = Level(b_satisfying3, "Have Fun 3 ", "This is a good level?", groups = [0,4,3], grid_size = 70)

b_satisfying4 = [[[4], [4], [4], [4], [4], [4], [4], [4], [4], [4, 6], [4]], [[4], [7], [], [3], [4], [], [], [], [], [6], [4]], [[4], [], [1], [], [1], [5], [1], [], [4], [], [4]], [[4], [3], [5], [], [], [], [4], [], [], [], [4]], [[4], [], [1], [], [1], [5], [4], [], [1], [], [4]], [[4], [], [], [], [5], [], [], [], [], [], [4]], [[4], [], [4], [], [4], [], [4, 6], [4], [1], [5], [4]], [[4], [], [4], [2], [], [], [], [], [], [], [4]], [[4], [], [1], [4], [1], [4], [1], [5], [1], [], [4]], [[4], [2], [], [], [], [], [], [], [], [], [4]], [[4], [4, 6], [4], [4], [4], [4], [4], [4], [4], [4], [4]]]
l_satisfying4 = Level(b_satisfying4, "Have Fun 4", groups = [0,4,3],  grid_size = 70)

b_merge = [[[4], [4, 6], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]], [[4], [], [], [], [], [], [], [], [], [], [], [4]], [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [], [], [], [], [], [], [], [], [3], [], [4]], [[4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [], [], [], [], [], [], [], [], [], [], [4]], [[4], [], [], [2], [2], [2], [2], [2], [], [], [], [4]], [[4], [], [], [2], [], [], [], [2], [], [], [], [4]], [[4], [], [], [2], [], [1], [], [2], [], [], [], [4]], [[4], [], [], [2], [], [], [], [2], [], [], [], [4]], [[4], [], [], [2], [2], [2], [2], [2], [], [], [], [4]], [[4], [], [], [], [], [], [], [], [], [], [], [4]], [[4], [], [], [], [], [], [], [], [], [], [], [4]], [[4], [4], [4], [4, 6], [4], [4], [4], [4],
        [4], [4], [4], [4]]]
l_merge = Level(b_merge, "Merge", "thanks to Braden for help designing", groups = [0,4,2], grid_size = 70)

b_rip = [[[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]], [[4], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [3], [4]], [[4], [], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [], [4]], [[4], [], [4], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [1], [7], [4], [], [4]], [[4], [], [4], [1], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [4], [], [4]], [[4], [], [4], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [1], [7], [7], [7], [4], [], [4]], [[4], [], [4],
        [7], [7], [1], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [4], [], [4]], [[4], [], [4], [7], [7], [7], [7], [7], [7], [7], [7], [1], [7], [7], [7], [7], [7], [4], [], [4]], [[4], [], [4], [7], [7], [7], [7], [1], [7], [7], [7], [7], [7], [7], [7], [7], [7], [4], [], [4]], [[4], [], [4], [7], [7], [7], [7], [7], [7], [1], [7], [7], [7], [7], [7], [7], [7], [4], [], [4]], [[4], [], [4], [7], [7], [7], [7], [7], [7], [3], [1], [7], [7], [7], [7], [7], [7], [4], [], [4]], [[4], [], [4], [7], [7], [7], [7], [7], [1], [7], [7], [7], [7], [7], [7], [7], [7], [4], [], [4]], [[4], [], [4], [7], [7], [7], [7], [7], [7], [7], [7], [7], [1], [7], [7], [7], [7], [4], [], [4]], [[4], [], [4], [7], [7], [7], [1], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [4], [], [4]], [[4], [], [4], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [1], [7], [7], [4], [], [4]], [[4], [], [4], [7], [1], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [4], [], [4]], [[4], [], [4], [2],
        [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [1], [4], [], [4]], [[4], [], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [], [4]], [[4], [2], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [4]], [[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]]]
l_rip = Level(b_rip, "R.I.P", "Good luck!", groups = [0,4,3], grid_size = 70)

b_tut1 = [[[1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [], [], [], [1], [], [], [], [1]], [[1], [], [1], [], [1], [], [1], [], [1]], [[1], [2], [1], [3], [1], [2], [1], [3], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [], [], [], [1], [], [], [], [1]], [[1], [], [1], [], [1], [], [1], [], [1]], [[1], [2], [1], [3], [1], [2], [1], [3], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_tut1 = Level(b_tut1, "The Main Mechanic", "Use the arrow keys (or just swipe on mobile!) to move the blue players onto the green goals")

b_tut2 = [[[1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [4], [], [], [], [4], [], [3], [1]], [[1], [], [], [], [], [], [], [], [1]], [[1], [2], [], [4], [], [], [], [4], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [], [], [], [], [], [], [3], [1]], [[1], [4], [], [4], [], [4], [], [4], [1]], [[1], [2], [], [], [], [], [], [], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_tut2 = Level(b_tut2, "Lava", "If any blue player touches red, the level restarts", [0,5])

b_tut3 = [[[1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [2], [], [], [], [], [], [3], 
[1]], [[1], [], [1], [1], [1], [1], [1], [1], [1]], [[1], [], [], [], [], [], [], [1], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [2], [], [], [], [], [3], [], [1]], [[1], 
[], [1], [1], [1], [1], [1], [1], [1]], [[1], [], [], [], [], [], [], [], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_tut3 = Level(b_tut3, "Simultaneous", "All players must be on a goal simultaneously to win", [0,5])

b_tut4 =[[[4], [4], [4], [1], [4], [1], [4], [4]], [[2], [], [], [], [], [], [], [3]], [[4], [1], [4], [4], [4], [4], [4], [1]], [[1], [1], [1], [1], [1], [1], [1], [1]], [[7], [], [], [], [4], [], [], []], [[4], [], [4], [], [], [], [4], [3]], [[2], [], [], [7], [4], [], [], [7]], [[1], [1], [1], [1], [1], [1], [1], [1]]]
l_tut4 = Level(b_tut4, "Coins", "All yellow coins must be collected before the goals will let you win", [0,5])

b_tut5 = [[[4], [2, 3], [3], [3], [3], [3], [3], [4]], [[1], [1], [1], [1], [1], [1], [1], [1]], [[1], [2], [], [6], [6], [], [], [1]], [[1], [1], [1], [1], [1], [1], [], [1]], [[1], [], [], [6], [6], [], [], [1]], [[1], [], [1], [1], [1], [1], [1], [1]], [[1], [], [], [], [], [], [], [3]], [[1], [1], [1], [6], [6], [1], [1], [1]]]
l_tut5 = Level(b_tut5, "Boulders", "If a player walks into a grey boulder, they stay still, and the boulder breaks", [0,5])

b_easymerge = b_level = [[[4], [3], [], [4], [], [6], [], [4]], [[4], [], [], [], [], [4], [6], []], [[4], [], [], [4], [], [], [], [4]], [[4], [4], [], [4], [], [], [], [4]], [[4], [], [], [4], [], [], [], [4]], [[4], [], [], [6], [], [4], [], [6]], [[], [], [], [4], [], [], [], [4]], [[4], [], [2], [], [], [2], [], [4]]]
l_easymerge = Level(b_easymerge, "The Illusion of Choice")

b_easyorange = [[[1], [1], [1], [1], [1], [1], [7], [7]], [[1], [1], [7], [], [7], [1], [], []], [[4], [1], [5], [4], [5], [1], [5], [5]], [[7], [5], [], [], [], [1], [], []], [[], [1], [], [2], [], [1], [2], []], [[7], [5], [], [], [], [1], [], [3]], [[1], [1], [5], [4, 6], [5], [1], [], []], [[1], [1], [7], [3], [7], [1], [], []]]
l_easyorange = Level(b_easyorange, "Order")

b_tutfinishes = [[[1], [1], [1], [1], [1], [1], [1], [4]], [[1], [1], [2, 3], [3], [3], [1], [1], [3, 2]], [[1], [1], [1], [1], [1], [1], [1], []], [[1], [1], [], [], [], [1], [1], [4]], [[1], [], [], [1], [], [], [1], [1]], [[2], [], [1], [1], [1], [], [], [1]], [[3], [1], [1], [1], [1], [1], [], []], [[], [], [], [], [], [], [], []]]
l_tutfinishes = Level(b_tutfinishes, "Early Bird", "You can move through and over goals freely, even if not all players are there at once (it won't help or hurt you)")

b_tutorange = [[[1], [1], [1], [1], [1], [1], [1], [1]], [[1], [7], [7], [7], [7], [7], [7], [1]], [[1], [5], [4], [4], [4], [4], [5], [1]], [[1], [], [], [3], [2], [], [], [1]], [[1], [1], [1], [1], [1], 
[1], [1], [1]], [[1], [], [], [], [], [], [], [1]], [[1], [], [], [3], [], [2], [5], [1]], [[1], [1], [1], [1], [1], [1], [1], [1]]]
l_tutorange = Level(b_tutorange, "Orange", "Orange squares turn red when the player stand on them: linger on the square at your peril!")

b_tutmerge = [[[1], [1], [1], [4], [4], [4], [4], [1]], [[1], [3], [1], [], [], [], [6], [1]], [[1], [5], [1], [], [], [], [], [1]], [[1], [], [5], [], [5], [5], [5], [1]], [[1], [], [], [2], [2], [], [], [1]], [[1], [], [], [2], [2], [], [], [1]], [[1], [4], [4], [4], [4], [4], [4], [1]], [[1], [1], [1], [1], [1], [1], [1], [1]]]
l_tutmerge = Level(b_tutmerge, "Merge", "If two players occupy the same square, they merge into one!")

#replaced
b_tut8 = [[[4, 6], [3], [1], [1], [1], [1], [1], [1]], [[4, 6], [], [1], [], [], [], [], [3]], [[4, 6], [], [1], [], [1], [1], [1], [1]], [[4, 6], [], [1], [], [], [], [], []], [[4, 6], [], [1], [1], 
[1], [1], [1], []], [[4, 6], [], [1], [], [], [], [], []], [[4, 6], [], [1], [], [1], [1], [1], [1]], [[4, 6], [2], [1], [], [], [], [], [2]]]
l_tut8 = Level(b_tut8, "Boulders on Lava", "Boulders can be on top of other features!", [0,5])

#Obsolete/unused
b_tut9 = [[[2], [], [3], [], [], [], [], [2]], [[1], [1], [1], [1], [5], [1], [1], [1]], [[2], [], [], [], [], [], [], [1]], [[1], [1], [5], [1], [1], [1], [1], [1]], [[1], [], [], [], [], [], [], [2]], [[1], [1], [1], [1], [1], [1], [5], [1]], [[], [], [2], [], [], [], [], [1]], [[3], [4, 6], [1], [1], [1], [1], [1], [1]]]
l_tut9 = Level(b_tut9, "Merge", "If two players end up on top of eachother, they fuse into one!", [0,5])


b_tut10 =[[[1], [1], [1], [1], [1], [1], [1], [1]], [[1], [1], [1], [5], [3], [5], [1], [1]], [[1], [1], [5], [5], [5], [5], [5], [1]], [[], [], [5], [5], [5], [5], [5], [1]], [[2], [], [5], [5], [5], [5], [5], [7]], [[1], [1], [5, 6], [5, 6], [5, 6], [5, 6], [5, 6], []], [[1], [1], [], [], [], [], [], []], [[1], [1], [1], [1], [1], [1], [1], [1]]]
l_tut10 = Level(b_tut10, "Boulders on Orange", "Remember: breaking a boulder takes time you may or may not have", [0,5])

#Perhaps not really a good tutorial level
b_tut11 =  [[[1], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7]], [[5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7]], [[5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 
7]], [[5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7]], [[5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7]], [[5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7], [5, 7]], [[], [1], [1], [1], [1], [1], [1], []], [[2], [1], [1], [1], [1], [1], [1], [3]]]
l_tut11 = Level(b_tut11, "Tutorial Complete!", "This level is impossible. To continue, select one of the above tabs like \'Easy\' to try a new level group. Have fun!", [0,5])

#Experimental level
b_exp1 = [[[3], [3], [3], [3], [3], [3], [3], [3], [3], [5], [1], [1], [4], [4], [3], [3], [3], [3], [3], [3]], [[3], [], [], [], [], [4], [1], [1], [1], [6], [], [1], [1], [1], [1], [5], [1], [4], [4], [3]], [[3], [], [], [], [], [], [5], [], [1], [1], [5], [], [1], [1], [1], [], [1], [4], [4], [3]], [[3], [], [], [], [4], [1], [1], [], [6], [1], [1], [], [1], [1], [5], [5, 6], [1], [1], [1], [3]], [[3], [], [4], [4], [4], [1], [1], [1], [5], [1], [1], [5], [1], [1], [5], [1], [1], [], [], [3]], [[3], [], [4], [1], [1], [1], [1], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [1], [5], [5], [1], [3]], [[3], [2], [], [5], [], [1], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [1], [], [1], [1], [3]], [[3], [], [4], [1], [6], [5], [7, 5], [7, 5], [7, 
5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [5], [6], [1], [4], [3]], [[3], [], [4], [1], [1], [1], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [1], [1], [4], [4], [3]], [[3], [], [4], [4], [4], [1], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [1], [1], [1], [1], [3]], [[3], [], [4], [1], [1], [1], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [5], [6], [1], [4], [3]], [[3], [], [4], [1], [6], [5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [1], [1], [], [5], [], [3]], [[3], [], [], [5], [], [1], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [1], [5], [1], [1], [1], [1], [1], [4], [3]], [[3], [], [4], [1], [1], [1], [7, 5], [7, 5], [7, 5], [7, 5], [7, 5], [1], [6], [], [1], [4], [4], [4], [4], [3]], [[3], [], [4], [4], [4], [4], [1], [1], [5], [1], [1], [1], [1], [5], [1], [4], [], [], [], [3]], [[3], [], [], [], [], [4], [4], [1], [6], [], [1], [4], [4], [], [4], [4], [], [], [], [3]], 
[[3], [], [], [], [], [], [4], [1], [1], [5], [1], [4], [], [], [], [], [], [], [], [3]], [[3], [], [], [], [], [], [4], [4], [4], [], [4], [4], [], [], [], [], [], [], [], [3]], [[3], [], [], [], [], 
[], [], [], [], [], [], [], [], [], [], [], [], [], [], [3]], [[3], [3], [3], [3], [3], [3], [3], [3], [3], [3], [3], [3], [3], [3], [3], [3], [3], [3], [3], [3]]]
l_exp1 = Level(b_exp1, "One Door", "Do it without trial and error :)", [0,6], grid_size = 40)

b_exp2 = [[[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [1], [4]], [[1], [3], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [4]], [[4], [], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [], [4]], [[4], [], [4], [5], 
[5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [1], [5], [4], [], [4]], [[4], [], [4], [1], [3], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [5], [4], [], [4]], [[4], [], [4], [5], [], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [], [5], [4], [], [4]], [[4], [], [4], [5], [], [5], [5], [5], [5], [1], [5], [5], [5], [5], [1], [5], [5], [5], [5], [5], [5], [], [5], [4], [], [4]], [[4], [], [4], [5], [], [5], [5], [1], [], [], [5], [5], [5], [5], [5], [5], [5], [5], [5], [1], [5], [], [5], [4], [], [4]], [[4], [], [4], [5], [], [5], [5], [5], [], [], [5], [5], [1], [3], [], [], [], [], [], [], [5], [], [5], [4], [], [4]], [[4], [], [4], [4], [], [4], [5], [5], [], [], [5], [5], [4], [], [4], [5], [5], [1], [5], [], [5], [], [5], [4], [], [4]], [[4], [], [4], [5], [2], [], [], [], [], [], [1], [], [], [2], [], [], [], [], [1], [], [5], [], [5], [4], [], [4]], [[4], [], [4], [4], [1], [], [], [], [], [], [], [], [4], [1], [4], [1], [], [], [], [], [1], [], [5], [4], [], [4]], [[4], [], [4], [5], [5], [], [1], [], [], [], [], [], [], [], [], [], [1], [5], [], [5], [5], [], [5], [4], [], [4]], [[4], [], [4], [1], [], [], [], [], [], [], [], [1], [], [], [], [], [], [], [], [5], [5], [], [5], [4], [], [4]], [[4], [], [4], [5], [], [], [], [1], [], [5], [5], [5], [], [], [], [], [], [], [], [1], [5], [], [5], [4], [], [4]], [[4], [], [4], [5], [], [1], [5], [5], [], [5], [5], [5], [1], [], [], [], [], [], [], [], [5], [], [5], [4], [], [4]], [[4], [], [4], [5], [], [], [], [], [], [], [], [], [], [], [], [], [], [1], [5], [], [5], [], [5], [4], [], [4]], [[4], [], [4], [5], [1], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [1], [], [5], [4], [], [4]], [[4], [], [4], [5], [5], 
[], [5], [4], [1], [5], [1], [5], [5], [], [], [], [], [], [1], [5], [5], [], [5], [4], [], [4]], [[4], [], [4], [5], [5], [], [1], [3], [], [], [], [4], [5], [1], [], [], [], [], [], [5], [5], [], [5], [4], [], [4]], [[4], [], [4], [5], [5], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [1], [5], [], [5], [4], [], [4]], [[4], [], [4], [5], [5], [1], [4], [2], [], [], [], [1], [5], [5], [], [], [], [], [], [], [], [], [1], [4], [], [4]], [[4], [], [4], [5], [5], [5], [4], [1], [4], [5], [4], [5], [5], [5], [1], [5], [5], [5], [5], [5], [5], [5], [5], [4], [], [4]], [[4], [], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [], [4]], [[4], [2], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [1]], [[4], [1], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]]]
l_exp2 = Level(b_exp2, "Cycle", "This might take a while", [0,6], grid_size = 25)

#Nice and easy
b_orangeline = [[[1], [3], [1], [1], [1], [1], [3], [1]], [[1], [7], [1], [1], [1], [1], [7], [1]], [[4], [5], [4], [4], [4], [4], [5], [4]], [[], [], [4], [], [], [], [], []], [[], [], [], [], [4], [], [], [4]], [[], [4], [4], [], [], [], [], []], [[2], [2], [], [], [1], [], [4], []], [[], [4], [1], [], [4], [], [], []]]
l_orangeline = Level(b_orangeline, "Aligned")

#Nice and easy
b_backforth = [[[1], [4], [4], [4, 6], [4], [4], [4], [1]], [[2, 3], [], [], [], [], [], [], []], [[1], [4], [4], [4], [4], [4], [4], [1]], [[2], [5], [5], [5, 7], [5], [5], [5], []], [[], [5], [5], [5], [5, 7], [5], [5], []], [[], [5], [5], [5, 7], [5], [5], [5], []], [[], [5], [5], [5], [5, 7], [5], [5], []], [[3], [5], [5], [5, 7], [5], [5], [5], []]]
l_backforth = Level(b_backforth, "Back and Forth") #Followup level "back and forth forever"

#Kinda nice, easy
b_clearing = [[[5], [5], [5], [5], [5], [5], [], []], [[3], [5], [5], [], [5], [5], [], [1]], [[2], [5], [5], [5], [5], [5], [], []], [[1], [1], [1], [1], [1], [1], [1], [1]], [[], [], [], [], [], [], [], [2]], [[4], [4], [4], [4], [4], [4], [5], []], [[3], [], [], [], [], [], [], []], [[4], [4], [4], [4], [4], [4], [4], [4]]]
l_clearing = Level(b_clearing, "Clearing")

#Not a greatly designed level, not too hard, easy
b_ok = [[[], [], [], [7], [7], [], [], []], [[5], [4, 6], [4, 6], [4], [4], [4], [4], [5]], [[], [2], [], [3], [], [], [], []], [[1], [1], [1], [1], [1], [1], [1], [1]], [[4], [4], [4], [4], [4], [4], [4], [4]], [[4, 6], [], [], [], [], [], [6], [4]], [[4, 6], [], [], [], [], [], [6], [4]], [[4, 6], [2], [], [3], [4, 6], [], [6], [4]]]
l_ok = Level(b_ok, "Options")

b_asym = [[[1], [1], [1], [4], [4], [4], [4], [1], [1], [1]], [[1], [1], [4], [], [], [], [], [4], [1], [1]], [[1], [4], [], [], [], [], [], [], [5], [1]], [[4], [], [], [5, 7], [5, 7], [5, 7], [5, 7], [], [], [4]], [[4], [], [], [5, 7], [7], [2, 3], [5, 7], [], [], [4]], [[4], [], [], 
[5, 7], [2, 3], [7], [5, 7], [], [], [4]], [[4], [], [], [5, 7], [5, 7], [5, 7], [5, 7], [], [], [4]], [[1], [4], [], [], [], [], [], [], [4], [1]], [[1], [1], [4], [], [], [], [], [4], [1], [1]], [[1], [1], [1], [4], [4], [4], [4], [1], [1], [1]]]
l_asym = Level(b_asym, "Broken Symmetry")

b_boulderlava2 = [[[4, 6], [3], [1], [1], [1], [1], [1], [1]], [[4, 6], [], [1], [], [], [], [], [3]], [[4, 6], [], [1], [], [4, 6], [4, 6], [4, 6], [4]], [[4, 6], [], [1], [], [], [], [], []], [[4, 6], [], [1], [4], [4], [4], [4], []], [[4, 6], [], [1], [], [], [], [], []], [[4, 6], [], [1], [], [1], [1], [1], [1]], [[4, 6], [2], [1], [], [], [], [], [2]]]
l_boulderlava2 = Level(b_boulderlava2, "Boulders on Lava", "Boulders can be on top of other features!")

b_tutfinale = [[[], [7], [1], [1], [3], [], [], []], [[], [4, 6], [1], [4], [4, 6], [], [5, 6], []], [[], [5], [3], [7], [], [1], [1], [7]], [[], [1], [1], [4], [], [1], [1], []], [[], [4, 6], [4], [4], [4], [], [5], []], [[], [], [], [], [], [], [4], [4, 6]], [[4], [4], [4], [5], [5], [4, 6], [4, 6], [7]], [[3], [2], [2], [], [], [2], [], []]]
l_tutfinale = Level(b_tutfinale, "Hmm...", "Getting tricky!")

b_zagswitch = [[[], [], [], [1], [3], [1], [4], [4]], [[], [1], [], [1], [], [1], [], [9]], [[], [1], [], [1], [], [1], [], [9]], [[], [1], [], [1], [], [1], [3], [9]], [[], [1], [], [1], [], [1], [], [9]], [[], [1], [], [1], [], [1], [], [9]], [[], [1], [], [1], [], [1], [2], [9]], [[2], [1], [], [], [], [1], [4], [4]]]
l_zagswitch = Level(b_zagswitch, "Zig-Zag", "Purple powers move in reverse!")

b_helpkey = [[[1], [1], [1], [1], [1], [9], [4], [3, 2]], [[1], [7, 5], [5], [], [], [], [3], [4]], [[1], [5], [7, 5], [5], [], [], [], [9]], [[1], [], [5], [5], [5], [], [], [1]], [[1], [], [], [5], [5], [5], [], [1]], [[9], [], [], [], [5], [7, 5], [5], [1]], [[], [], [], [], [], [5], [5, 7], [1]], [[2], [], [9], [1], [1], [1], [1], [1]]]
l_helpkey = Level(b_helpkey, "Shortcuts", "you might find the f key helpful here")

b_swapmaze = [[[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]], [[4], [9], [], [], [], [9], [], [], [], [9], [4], [], [], [], [], [], [], [], [], [], [4]], [[4], [], [1], [], [1], [4], [1], [], [1], [], [4], [], [1], [4], [1], [], [1], [], [1], [], [4]], [[4], [], [4], [], [], [], [], [], [], [], [4], [], [], [], [], [], [], [], [], [], [4]], [[4], [], [1], [], [1], [], [1], [], [1], [4], [4], [], [1], [], [1], [], [1], [4], [1], [], [4]], [[4], [], [], [], [], [], [], [9], [], [], [4], [], [], [3], [4], [], [4], [], [], [], [4]], [[4], [], [1], [4], [1], [], [1], [], [1], [], [4], [4], [1], [], [1], [], [1], [], [1], [], [4]], [[4], [], [], [], [], [], [4], [], [], [], [4], [], [], [], [], [], [], [9], [], [], [4]], [[4], [], [1], [4], [1], [], [1], [], [1], [], [4], [], [1], [], [1], [], [1], [], [1], [], [4]], [[4], [], [], [3, 2], [4], [], [], [], [4], [], [4], [], [], [2], [], [], [], [], [4], [9], [4]], [[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]]]
l_swapmaze = Level(b_swapmaze, "Swap-maze", "warning: maze may be larger than it appears")

b_random = [[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [], [], [1], [], [1], [1], [], [5], [], [], [1], [1]], [[1], [1], [], [1], [], [], [1], [], [3], [2], [], [], [1]], [[1], [1], [4], [], [], [5], [1], [], [], [4], [], [], [1]], [[1], [3], [], [2], [], [], [1], [6], [5], [1], [1], [1], [1]], [[1], [4], [4], [], [4], [3], [1], [], [], [], [], [1], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_random = Level(b_random, "Random", "This level was randomly generated! Credit to Drake Thomas")

b_random2 =[[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [], [1], [], [], [1], [6], [], [], [2], [1]], [[1], [], [], [2], [4], [1], [], [], [], [3], [1]], [[1], [], [], [], [5], [1], [1], [], [], [], [1]], [[1], [1], [4], [3], [], [1], [1], [1], [1], [], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_random2 = Level(b_random2, "Random 2", "This level was randomly generated! Credit to Drake Thomas")

b_level3 =[[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [2], [], [3], [1], [2], [1], [4], [1], [], [1], [], [1]], [[1], [1], [], [], [1], [], [3], [], [1], [3], [], [], [1]], [[1], [], [], [3], [1], [], [1], [4], [1], [5], [2], [4], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]] 
l_level3 = Level(b_level3, "Random", "This level was randomly generated! Credit to Drake Thomas")

b_level4 = [[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [], [1], [3], [1], [5], [1], [2], [1], [], [], [4], [1]], [[1], [4], [4], [], [1], [], [3], [], [1], [], [1], [], [1]], [[1], [], [], [2], [1], [6], [1], [6], [1], [3], [2], [], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_level4 = Level(b_level4, "Random")

b_level5 = [[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
 [[1], [6], [1], [2], [1], [], [4], [1], [1], [], [2], [], [1]],
 [[1], [3], [6], [], [1], [], [], [2], [1], [], [1], [], [1]],
 [[1], [], [], [4], [1], [6], [4], [3], [1], [1], [], [3], [1]],
 [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_level5 = Level(b_level5, "Random")

b_figureeight = [[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [], [], [], [], [1], [1], [], [2], [], [1]], [[1], [], [4], [4], [], [1], [], [4], [4], [], [1]], [[1], [], [1], [1], 
[3], [1], [], [4], [4], [], [1]], [[1], [], [7], [1], [2], [1], [3], [], [], [], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_figureeight = Level(b_figureeight, "Loop")

b_hardgood = [[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [], [], [3], [4], [1], [], [], [], [], [1]], [[1], [], [], [4], [1], [1], [7], [1], [], [], [1]], [[1], [], [], [2], [4], [1], 
[1], [4], [], [1], [1]], [[1], [], [4], [], [], [1], [2], [], [], [3], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_hardgood = Level(b_hardgood, "Good morning!")

b_glorious = [[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [6], [4], [6], [3], [1], [6], [], [], [2], [1]], [[1], [2], [], [], [4], [1], [], [], [], [], [1]], [[1], [], [4], [4], [1], [1], [], [1], [6], [3], [1]], [[1], [4], [1], [1], [1], [1], [1], [], [], [], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_glorious = Level(b_glorious, "Your proof is wrong","'With man this is impossible, but with God all things are possible.\'")

b_thin = [[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]], [[1], [2], [1], [], [4], [], [], [6], [], [4], [3], [1], [2], [], [], [], [], [], [], [3], [4], [7], [1]], [[1], [], [], [], [], [], [], [], [6], [6], [], [1], [], [4], [5], [1], [], [4], [], [], [], [], [1]], [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]]
l_thin = Level(b_thin, "Snek attack")

b_thin2 =[[[1], [2], [1], [], [], [], [], [1], [4], [], [6], [], [], [1], [2], [], [], [], [4], [1]], [[4], [], [5], [], [], [4], [], [], [], [], [1], [4], [], [6], [], [5], [1], [], [3], [1]]]
l_thin2 = Level(b_thin2, "Snek attack 2")