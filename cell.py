import pygame
from settings import Settings
import game_states as game_states


class Cell:
    """This class represents a single Cell in the game"""

    def __init__(self, screen, x, y):
        """Initialize the cell with an x and y position"""

        # import game settings
        settings = Settings()
        # keep track of cell's states
        self.alive = False
        # grab screen where cell will be placed
        self.screen = screen
        # x and y are passed when cell is created
        self.x = x
        self.y = y
        # width and height are stored in global settings
        self.width = settings.cell_width
        self.height = settings.cell_height
        # colors are represented with tuples
        self.dead_color = (0, 0, 0)
        self.alive_color = (255, 255, 20)
        # a line width of one fills the shape
        self.dead_line_width = 1
        self.alive_line_width = 0

    def draw(self):
        """Draws the cell on the screen"""

        # if the cell is dead, draw an empty black square
        # if it is alive, draw a filled yellow square
        if not self.alive:
            pygame.draw.rect(self.screen, self.dead_color,
                             [self.x, self.y, self.width, self.height], self.dead_line_width)
        else:
            pygame.draw.rect(self.screen, self.alive_color,
                             [self.x, self.y, self.width, self.height], self.alive_line_width)

    """change the state of the cell when the mouse is drug over it"""

    def change_on_drag(self):
        # if the cell is dead, make it alive
        if not self.alive:
            self.alive = True
        else:
            self.alive = False
