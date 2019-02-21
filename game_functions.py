import sys
import pygame


def check_events():
    """Respond to keypresses and mouse events"""
    # watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()


def upadte_screen(screen: object, settings: object, cell_grid: object):
    """Update images on the screen and 'flip' to a new screen"""

    # draw the screens background
    screen.fill(settings.bg_color)
    # redraw the cells
    for col in cell_grid:
        for cell in col:
            cell.draw()
    # make the most recently drawn screen visible
    pygame.display.flip()
