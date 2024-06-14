import pygame
import pygame.freetype
pygame.init()

# Initializing the dimensions of the screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
BRIGHT_RED = (255,0,0)
BRIGHT_GREEN = (0,255,0)
BRIGHT_BLUE = (0,0,255)
BRIGHT_PURPLE = (189,109,232)
BRIGHT_PURPLE2 = (255,0,255)

# Setting up button dimensions
TITLE_WIDTH = 400
MENU_BUTTON_WIDTH = 400
MENU_BUTTON_HEIGHT = 95
HOME_BUTTON_WIDTH = 100

# Setting up button functions
MENU_BUTTON_COUNT = 4

# Menu Functionality
on_menu = True

# Setting up the graph
NODE_COUNT = 8
EDGE_COUNT = 8
GRAPH_SETUP = [[], [[2,3], [3,6]], [[1,3], [4,5],[7,3]], [[1,6], [6,1], [7,2]], [[2,5], [5,10], [8,4]], [[4,10]], [[3,1]], [[3,2],[2,3]], [[4,4]]]

# Setting up fonts
title_font = pygame.freetype.Font("freedomfont.ttf",80)
algorithm_title_font = pygame.freetype.Font("freedomfont.ttf",60)
learn_more_font = pygame.freetype.Font('freedomfont.ttf',45)
menu_button_font = pygame.freetype.Font("freedomfont.ttf",30)
node_font = pygame.freetype.Font('aovelsans.ttf',30)
TEXT_OFFSET = 10

# Visualiser Timer
visualiser_timer = 0

# Graph Theory Algorithm Edge Lengths
EDGE_COLOR = BRIGHT_GREEN
BFS_EDGE = 7
cur_bfs_edge = 0
temp_bfs_visited = [False] * NODE_COUNT

DFS_EDGE = 7
cur_dfs_edge = 0
temp_dfs_visited = [False] * NODE_COUNT

DIJKSTRAS_EDGE = 7
cur_dijkstras_edge = 0
temp_dijkstras_visited = [False] * NODE_COUNT

KRUSKALS_EDGE = 7
cur_kruskal_edge = 0
temp_kruskals_visited = [False] * NODE_COUNT

# Collision Detection
def is_collision(mx,my,x1,y1,x2,y2):
    return mx >= x1 and mx <= x2 and my >= y1 and my <= y2

def midpoint(x1,y1,x2,y2):
    xval = (x1+x2)/2
    yval = (y1+y2)/2
    return (xval,yval)