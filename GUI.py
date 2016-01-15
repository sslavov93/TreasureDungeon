import pygame
import inputbox


class GraphicalUserInterface():
    def __init__(self):
        self.colors = {"Z": "black", "#": "black", ".": "white", "H": "green",
                       "O": "red", "C": "brown", "K": "yellow"}
        self.color_codes = {"black": (0, 0, 0), "white": (255, 255, 255),
                            "green": (0, 255, 0), "red": (255, 0, 0),
                            "blue": (0, 0, 255), "brown": (137, 76, 46),
                            "yellow": (255, 255, 0)}

    def __get_dungeon_dimentions(self):
        pass

pygame.init()
ss = width, height = 1024, 600
screen = pygame.display.set_mode(ss)
inp = int(inputbox.ask(screen, 'Message'))


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
