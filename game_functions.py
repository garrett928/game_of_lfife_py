import sys
import pygame
from settings import Settings

# global var
mouse_drag = False
settings = Settings()

def check_events():
    """Respond to keypresses and mouse events"""
    global mouse_drag
    # watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        # if the mouse button is pushed than start dragging
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_drag = True
            print("mouse down")
        # if the mouse button is released than stop dragging
        if event.type == pygame.MOUSEBUTTONUP:
            print("mouse up")
            mouse_drag = False

    # if the mouse is being dragged than
    if mouse_drag:
        mouse_pos = pygame.mouse.get_pos()
        cell_at_mouse_pos = (mouse_pos[0] // settings.cell_width,
                             mouse_pos[1] // settings.cell_height)
        print("mouse pos: " + str(cell_at_mouse_pos))


def update_screen(screen: object, settings: object, cell_grid: object):
    """Update images on the screen and 'flip' to a new screen"""

    # draw the screens background
    screen.fill(settings.bg_color)
    # redraw the cells
    for col in cell_grid:
        for cell in col:
            cell.draw()
    # make the most recently drawn screen visible
    pygame.display.flip()
