import pygame
from map_validator import MapValidator
from dungeon import Dungeon
import sys
import os


class GraphicalUserInterface():
    def __init__(self):
        self.exit = False
        self.is_created = False
        self.map_loaded = False
        self.validator = None
        self.input = None

        self.colors = {"Z": "grey", "#": "black", ".": "white", "H": "green",
                       "O": "red", "C": "brown", "K": "yellow",
                       "S": "blue", "N": "red"}
        self.color_codes = {
            "black": (0, 0, 0), "white": (255, 255, 255), "green": (0, 255, 0),
            "red": (255, 0, 0), "brown": (153, 76, 0), "yellow": (255, 255, 0),
            "blue": (0, 0, 255), "grey": (128, 128, 128)}

    def load_map(self, map_path):
        self.validator = MapValidator(map_path)
        if not self.validator.validate_map():
            return self.validator.generate_message()
        else:
            self.dungeon = Dungeon(map_path)
            if self.dungeon.map:
                self.map_loaded = True
                self.grid = self.dungeon.convert_map_to_changeable_tiles()
                self.map_row = len(self.grid)
                self.map_col = len(self.grid[0])
                return self.validator.generate_message()

    def display_map(self):
        cell_width = 20
        cell_height = 20
        cell_margin = 5

        scr_width = (cell_margin + cell_width) * self.map_col + cell_margin
        scr_height = (cell_margin + cell_height) * self.map_row + cell_margin

        ss = [scr_width, scr_height]
        screen = pygame.display.set_mode(ss)

        pygame.display.set_caption("Treasure Dungeon")
        pygame.init()
        for row in range(self.map_row):
            for column in range(self.map_col):
                color = self.color_codes[self.colors[self.grid[row][column]]]
                pygame.draw.rect(
                    screen,
                    color,
                    [(cell_margin + cell_width) * column + cell_margin,
                     (cell_margin + cell_height) * row + cell_margin,
                     cell_width, cell_height])
        done = False
        # # Used to manage how fast the screen updates
        # clock = pygame.time.Clock()

        pygame.display.flip()

        # make this global for every object
        while not done:
            for event in pygame.event.get():
                print(event.type)
                if event.type == pygame.QUIT:
                    done = True

        pygame.quit()

    def start(self):
        self.display_map()


def run():
    map_location = sys.argv[1] if len(sys.argv) > 1 else None
    gui = GraphicalUserInterface()
    if map_location and os.path.exists(map_location):
        if not gui.map_loaded:
            gui.load_map(map_location)
            if gui.map_loaded:
                gui.start()
    return None

run()


# GUI.draw_map()
# # This sets the WIDTH and HEIGHT of each grid location
# WIDTH = 20
# HEIGHT = 20

# # This sets the margin between each cell
# MARGIN = 5

# # Create a 2 dimensional array. A two dimensional
# # array is simply a list of lists.
# grid = []
# for row in range(10):
#     # Add an empty array that will hold each cell
#     # in this row
#     grid.append([])
#     for column in range(10):
#         grid[row].append(0)  # Append a cell

# # Set row 1, cell 5 to one. (Remember rows and
# # column numbers start at zero.)
# grid[1][5] = 1

# # Initialize pygame
# pygame.init()

# # Set the HEIGHT and WIDTH of the screen
# WINDOW_SIZE = [255, 255]
# screen = pygame.display.set_mode(WINDOW_SIZE)

# # Set title of screen
# pygame.display.set_caption("Array Backed Grid")

# # Loop until the user clicks the close button.
# done = False

# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()

# # -------- Main Program Loop -----------
# while not done:
#     for event in pygame.event.get():  # User did something
#         if event.type == pygame.QUIT:  # If user clicked close
#             done = True  # Flag that we are done so we exit this loop
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # User clicks the mouse. Get the position
#             pos = pygame.mouse.get_pos()
#             # Change the x/y screen coordinates to grid coordinates
#             column = pos[0] // (WIDTH + MARGIN)
#             row = pos[1] // (HEIGHT + MARGIN)
#             # Set that location to zero
#             grid[row][column] = 1
#             print("Click ", pos, "Grid coordinates: ", row, column)

#     # Set the screen background
#     screen.fill(BLACK)

#     # Draw the grid
#     for row in range(10):
#         for column in range(10):
#             color = WHITE
#             if grid[row][column] == 1:
#                 color = GREEN
#             pygame.draw.rect(screen,
#                              color,
#                              [(MARGIN + WIDTH) * column + MARGIN,
#                               (MARGIN + HEIGHT) * row + MARGIN,
#                               WIDTH,
#                               HEIGHT])

#     # Limit to 60 frames per second
#     clock.tick(60)

#     # Go ahead and update the screen with what we've drawn.
#     pygame.display.flip()

# # Be IDLE friendly. If you forget this line, the program will 'hang'
# # on exit.
# pygame.quit()
