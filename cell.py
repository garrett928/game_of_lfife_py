import pygame
from settings import Settings

class Cell:
    """This class represents a single Cell in the game"""

    def __init__(self, screen, x, y):
        """Initialize the cell with an x and y position"""

        settings = Settings()

        self.screen = screen
        self.x = x
        self.y = y
        self.width = settings.cell_width
        self.height = settings.cell_height
        self.color = (0, 0, 0)
        self.line_width = 0

    def draw(self):
        """Draws the cell on the screen"""
        pygame.draw.rect(self.screen, self.color,
                         [self.x, self.y, self.width, self.height], self.line_width)
