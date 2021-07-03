# MODULES
import pygame, sys
import numpy as np
import copy

# initializes pygame
pygame.init()

#CONSTANTS
DEFAULT_GRID_SIZE = 100
global GRID_SIZE
GRID_SIZE = 100
DEFAULT_NUM_ROWS = 5
DEFAULT_NUM_COLS = 5
# rgb: red green blue
WHITE = (255, 255, 255)
LIGHT_GREY = (230, 230, 230)
DARK_GREY = (100,100,100)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
ORANGE = (255,165,0)
YELLOW = (255,230,0)
#Now for things specific to game
EVEN_COLOR = WHITE
ODD_COLOR = LIGHT_GREY
PLAYER_COLOR = BLUE
WALL_COLOR = BLACK
FINISH_COLOR = GREEN
DEATH_COLOR = RED
COLLAPSE_COLOR = ORANGE
BARRIER_COLOR = DARK_GREY
COIN_COLOR = YELLOW
#a sort of purple
PLAYER2_COLOR = (128, 0, 128)
PLAYER_BOTH = (107, 52, 235)
PILL_COLOR = (235, 52, 220)
TELEPORTER_COLORS = 20*[RED, ORANGE, YELLOW, GREEN, BLUE, PLAYER2_COLOR]

#KEY FOR INTERPRETING ARRAY
WALL = 1
PLAYER1 = 2
FINISH1 = 3
DEATH = 4
COLLAPSE = 5
BARRIER = 6
COIN = 7
PLAYER2 = 8
PILL = 9
TELEPORTER_1 = 100

def zero_filled(rows, cols):
    return [[0]*cols for i in range(rows)]

def empty_filled(rows, cols):
    return [[[]]*cols for i in range(rows)]

def empty_filled2(rows, cols):
    return [[[] for i in range(cols)] for i in range(rows)]

#Usually our boards hold in each cell on a 2d grid a list of feautures there,
#but sometimes we want to initialize with just a 2d grid of ints
def wrap(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = [board[i][j]]

#This does the "opposite"
def unwrap(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == []:
                board[i][j] = 0
            else:
                board[i][j] = board[i][j][0]

def remove_duplicates(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = list(dict.fromkeys(arr[i][j]))

class Level():
    def __init__(self, init_board, name, description = " ", groups = [0], grid_size = DEFAULT_GRID_SIZE):
        if type(init_board[0][0]) != type([]):
            wrap(init_board)
            self.board = init_board
        else:
            self.board = init_board
        self.name = name
        self.num_rows = len(self.board)
        self.num_cols = len(self.board[0])
        self.grid_size = grid_size
        self.groups = groups
        self.description = description
    
    def set_group(self, arr):
        self.groups = arr


    def is_passable(self, row, col):
        if row < 0 or col < 0:
            return False
        try:
            return (not 1 in self.board[row][col] and not 6 in self.board[row][col] and not -6 in self.board[row][col])
        except:
            return False
    
    def break_barrier(self, row, col):
        if row < 0 or col < 0 or row >= self.num_rows or col >= self.num_cols:
            return
        while 6 in self.board[row][col]:
            self.board[row][col].remove(6)
            self.board[row][col].append(-6)
    
    def remove_boulder_ghosts(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                in_cell = self.board[i][j]
                while (-6 in in_cell):
                    self.board[i][j].remove(-6)

    
    def remove_duplicates(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if 2 in self.board[i][j]:
                    while 2 in self.board[i][j]:
                        self.board[i][j].remove(2)
                    self.board[i][j].append(2)
                if PLAYER2 in self.board[i][j]:
                    while PLAYER2 in self.board[i][j]:
                        self.board[i][j].remove(PLAYER2)
                    self.board[i][j].append(PLAYER2)
    
    def make_positive(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.board[i][j] = list(map(lambda x: abs(x), self.board[i][j]))
    
    def move_north(self):
        explode = False
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if 2 in self.board[i][j]:
                    if self.is_passable(i-1, j):
                        self.board[i][j].remove(2)
                        self.board[i-1][j].append(-2)
                    self.break_barrier(i-1, j)
                if self.test_explosion():
                    explode = True
                if PLAYER2 in self.board[i][j]:
                    if self.is_passable(i+1, j):
                        self.board[i][j].remove(PLAYER2)
                        self.board[i+1][j].append(-PLAYER2)
                    self.break_barrier(i+1, j)
                if self.test_explosion():
                    explode = True
        self.remove_boulder_ghosts()
        self.make_positive()
        return explode

    def move_south(self):
        explode = False
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if 2 in self.board[i][j]:
                    if self.is_passable(i+1, j):
                        self.board[i][j].remove(2)
                        self.board[i+1][j].append(-2)
                    self.break_barrier(i+1, j)
                if self.test_explosion():
                    explode = True
                if PLAYER2 in self.board[i][j]:
                    if self.is_passable(i-1, j):
                        self.board[i][j].remove(PLAYER2)
                        self.board[i-1][j].append(-PLAYER2)
                    self.break_barrier(i-1, j)
                if self.test_explosion():
                    explode = True
        self.remove_boulder_ghosts()
        self.make_positive()
        return explode

    def move_east(self):
        explode = False
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if 2 in self.board[i][j]:
                    if self.is_passable(i, j+1):
                        self.board[i][j].remove(2)
                        self.board[i][j+1].append(-2)
                    self.break_barrier(i, j+1)
                if self.test_explosion():
                    explode = True
                if PLAYER2 in self.board[i][j]:
                    if self.is_passable(i, j-1):
                        self.board[i][j].remove(PLAYER2)
                        self.board[i][j-1].append(-PLAYER2)
                    self.break_barrier(i, j-1)
                if self.test_explosion():
                    explode = True
        self.remove_boulder_ghosts()
        self.make_positive()
        return explode

    def move_west(self):
        explode = False
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if 2 in self.board[i][j]:
                    if self.is_passable(i, j-1):
                        self.board[i][j].remove(2)
                        self.board[i][j-1].append(-2)
                    self.break_barrier(i, j-1)
                if self.test_explosion():
                    explode = True
                if PLAYER2 in self.board[i][j]:
                    if self.is_passable(i, j+1):
                        self.board[i][j].remove(PLAYER2)
                        self.board[i][j+1].append(-PLAYER2)
                    self.break_barrier(i, j+1)
                if self.test_explosion():
                    explode = True
        self.remove_boulder_ghosts()
        self.make_positive()
        return explode

    def won(self):
        for i in self.board:
            for j in i:
                if ((2 in j or -2 in j or PLAYER2 in j or -1*PLAYER2 in j) and not 3 in j) or COIN in j:
                    return False
        return True

    def lost(self):
        for i in self.board:
            for j in i:
                if (2 in j or -2 in j or PLAYER2 in j or -PLAYER2 in j) and 4 in j:
                    return True
                #if ((2 in j or -2 in j) and (PLAYER2 in j or -PLAYER2 in j)):
                #    return True
        return False
    
    def test_explosion(self):
        return False
        '''
        for i in self.board:
            for j in i:
                if ((2 in j or -2 in j) and (PLAYER2 in j or -PLAYER2 in j)):
                    return True
        return False
        '''

    def collapse_to_death(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                in_cell = self.board[i][j]
                if (2 in in_cell or -2 in in_cell or PLAYER2 in in_cell or (-1)*PLAYER2 in in_cell) and 5 in in_cell:
                    self.board[i][j].remove(5)
                    self.board[i][j].append(4)

    def pick_up_coin(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                in_cell = self.board[i][j]
                while (2 in in_cell  or -2 in in_cell or PLAYER2 in in_cell or -PLAYER2 in in_cell) and COIN in in_cell:
                    self.board[i][j].remove(COIN)

    def reverse_player(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                in_cell = self.board[i][j]
                if (2 in in_cell):
                    self.board[i][j].remove(2)
                    self.board[i][j].append(PLAYER2)
                elif (PLAYER2 in in_cell):
                    self.board[i][j].remove(PLAYER2)
                    self.board[i][j].append(PLAYER1)
    
    def pick_up_pill(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                in_cell = self.board[i][j]
                while (2 in in_cell and PILL in in_cell):
                    self.board[i][j].remove(PILL)
                    self.board[i][j].remove(2)
                    self.board[i][j].append(PLAYER2)
                while (PLAYER2 in in_cell and PILL in in_cell):
                    self.board[i][j].remove(PILL)
                    self.board[i][j].remove(PLAYER2)
                    self.board[i][j].append(PLAYER1)

    def activate_teleporters(self):
        for tele in range(100,200):
            locations = []
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    if tele in self.board[i][j]:
                        locations += [[i,j]]
            if len(locations) == 0:
                continue
            if len(locations) != 2:
                raise Exception
            for item in [PLAYER1, PLAYER2]:
                if item in self.board[locations[0][0]][locations[0][1]]:
                    print("HERE WE GO")
                    self.board[locations[0][0]][locations[0][1]].remove(item)
                    self.board[locations[1][0]][locations[1][1]].append(item)
                elif item in self.board[locations[1][0]][locations[1][1]]:
                    print("HERE WE GO")
                    self.board[locations[1][0]][locations[1][1]].remove(item)
                    self.board[locations[0][0]][locations[0][1]].append(item)

def drawGrid(screen, board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            #This if/else just for background
            if (row+col) % 2 == 0:
                r = pygame.Rect((col*GRID_SIZE, row*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, EVEN_COLOR, r)
            else:
                rr = pygame.Rect((col*GRID_SIZE, row*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, ODD_COLOR, rr)
            if 1 in board[row][col]:
                r = pygame.Rect((col*GRID_SIZE, row*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, WALL_COLOR, r)
            if 3 in board[row][col]:
                r = pygame.Rect((col*GRID_SIZE, row*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, FINISH_COLOR, r)
            if 4 in board[row][col]:
                r = pygame.Rect((col*GRID_SIZE, row*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, DEATH_COLOR, r)
            if 5 in board[row][col]:
                r = pygame.Rect((col*GRID_SIZE, row*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, COLLAPSE_COLOR, r)
            if 6 in board[row][col]:
                r = pygame.Rect((col*GRID_SIZE+6, row*GRID_SIZE+6), (GRID_SIZE-12, GRID_SIZE-12))
                pygame.draw.rect(screen, BARRIER_COLOR, r)
            if 2 in board[row][col] and not PLAYER2 in board[row][col]:
                r = pygame.Rect((col*GRID_SIZE+6, row*GRID_SIZE+6), (GRID_SIZE-12, GRID_SIZE-12))
                pygame.draw.rect(screen, PLAYER_COLOR, r)
            if PLAYER2 in board[row][col] and not 2 in board[row][col]:
                r = pygame.Rect((col*GRID_SIZE+6, row*GRID_SIZE+6), (GRID_SIZE-12, GRID_SIZE-12))
                pygame.draw.rect(screen, PLAYER2_COLOR, r)
            if 2 in board[row][col] and PLAYER2 in board[row][col]:
                r = pygame.Rect((col*GRID_SIZE+6, row*GRID_SIZE+6), (GRID_SIZE-12, GRID_SIZE-12))
                pygame.draw.rect(screen, PLAYER_BOTH, r)
            if 7 in board[row][col]:
                r = pygame.Rect((col*GRID_SIZE+8, row*GRID_SIZE+8), (GRID_SIZE-16, GRID_SIZE-16))
                pygame.draw.rect(screen, COIN_COLOR, r)
            if PILL in board[row][col]:
                r = pygame.Rect((col*GRID_SIZE+10, row*GRID_SIZE+10), (GRID_SIZE-20, GRID_SIZE-20))
                pygame.draw.rect(screen, COLOR, r)
            for i in range(100, 200):
                if i in board[row][col]:
                    COLOR = TELEPORTER_COLORS[i-100]
                    r1 = pygame.Rect((col*GRID_SIZE, row*GRID_SIZE), (GRID_SIZE, 10))
                    pygame.draw.rect(screen, COLOR, r1)
                    r2 = pygame.Rect((col*GRID_SIZE, row*GRID_SIZE), (10, GRID_SIZE))
                    pygame.draw.rect(screen, COLOR, r2)
                    r3 = pygame.Rect(((col+1)*GRID_SIZE-10, row*GRID_SIZE), (10, GRID_SIZE))
                    pygame.draw.rect(screen, COLOR, r3)
                    r4 = pygame.Rect((col*GRID_SIZE, (row+1)*GRID_SIZE-10), (GRID_SIZE, 10))
                    pygame.draw.rect(screen, COLOR, r4)

def level_editor(num_rows = DEFAULT_NUM_ROWS, num_cols = DEFAULT_NUM_COLS, level_input = []):
    if level_input != []:
        board = level_input.board
        num_rows = level_input.num_rows
        num_cols = level_input.num_cols
    else:
        board = empty_filled2(num_rows, num_cols)
    m = max(num_rows, num_cols)
    global GRID_SIZE
    GRID_SIZE = int(800/m)

    screen = pygame.display.set_mode((GRID_SIZE*num_cols, GRID_SIZE*num_rows))
    pygame.display.set_caption("LEVEL EDITOR")
    current_placement = 0
    while True:
        pygame.display.set_caption("w:wall e:clear p:player f:finish d:death o:orange b:boulder c:coin r:reversed player s:pill")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                current_placement = 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                current_placement = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                current_placement = 2
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                current_placement = 3
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                current_placement = 4
            if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                current_placement = 5
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                current_placement = 6
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                current_placement = 7
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                current_placement = PLAYER2
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                current_placement = PILL
            #Teleporters
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                current_placement = 100
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                current_placement = 101
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                current_placement = 102
            if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                current_placement = 103
            if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                current_placement = 104
            if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                current_placement = 105
            #printing
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                remove_duplicates(board)
                print("b_level = ", end = "")
                print(board)
                print("l_level = Level(b_level, name, description, groups)")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                remove_duplicates(board)
                play_level(Level(board, "Testing level: hit escape to reenter editor", grid_size = GRID_SIZE))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0] # row
                mouseY = event.pos[1] # col
                clicked_row = int(mouseY // GRID_SIZE)
                clicked_col = int(mouseX // GRID_SIZE)
                if current_placement == 0:
                    board[clicked_row][clicked_col] = []
                else:
                    board[clicked_row][clicked_col].append(current_placement)
            drawGrid(screen, board)
            pygame.display.update()
        drawGrid(screen, board)
        pygame.display.update()

def play_level(level_original):
    level = copy.deepcopy(level_original)
    remove_duplicates(level.board)
    saved_level = copy.deepcopy(level)
    num_rows = level.num_rows
    num_cols = level.num_cols
    m = max(num_rows, num_cols)
    global GRID_SIZE
    GRID_SIZE = int(800/m)
    board = level.board
    screen = pygame.display.set_mode((GRID_SIZE*num_cols, GRID_SIZE*num_rows))
    pygame.display.set_caption(level.name)
    playing = True
    explosion = False
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                sys.exit()
            if event.type == pygame.KEYUP:
                continue
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                level = copy.deepcopy(level_original)
                board = level.board
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                explosion = level.move_north() or explosion
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                explosion = level.move_south() or explosion
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                explosion = level.move_east() or explosion
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                explosion = level.move_west() or explosion
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                level.reverse_player()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                playing = False 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                saved_level = saved_level = copy.deepcopy(level)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                level = copy.deepcopy(saved_level)
                board = level.board
            if level.lost() or level.test_explosion(): #Have "or explosion" here to have strong canceling: change some code elsewhere
                level = copy.deepcopy(level_original)
                board = level.board
                explosion = False
            elif level.won():
                playing = False
            level.activate_teleporters()
            level.collapse_to_death()
            level.remove_duplicates()
            level.pick_up_coin()
            level.pick_up_pill()
        drawGrid(screen, board)
        pygame.display.update()

#PRINT CODE
#print("Hello stackoverflow!", file=open("output.txt", "a"))
def print_level(level):
    result = "{\n   \"name\": \""
    result += level.name
    result += "\","
    result += "\n   \"groups\": "
    result += str(level.groups)
    result += ",\n   \"description\": \""
    result += level.description
    result += "\",\n   \"definition\": "
    result += str(level.board)
    result += "\n   }"
    return result

def make_json(levels):
    result = ("{\n  \"groups\": [\"All\", \"Easy\", \"Medium\", \"Hard\", \"Classic\", \"Tutorial\",\"Experimental\", \"Random\", \"Curated\"],\n\"puzzles\": [")
    for i in levels:
        result += "\n   "
        result += print_level(i)
        result += ","
    result = result[:-1]
    result += "\n]\n}"
    with open("C:\\Users\\beren\\Documents\\GIT\\Multimaze\\pages\\levels.json", 'r+') as f:
        f.truncate(0)
    print(result, file=open("C:\\Users\\beren\\Documents\\GIT\\Multimaze\\pages\\levels.json", "a"))
    with open("levels.json", 'r+') as f:
        f.truncate(0)
    print(result, file=open("levels.json", "a"))