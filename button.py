import pygame


class Button:
    """A class to handle displaying and using a button on scrren"""

    def __init__(self, screen, name, x, y, width, height):
        self.screen = screen
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.line_width = 0
        self.color = (200, 200, 200)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height], self.line_width)

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < self.x + self.width and mouse_pos[0] > self.x \
                and mouse_pos[1] < self.y + self.height and mouse_pos[1] > self.y:

            if pygame.mouse.get_pressed():
                return True

        else:
            return False
