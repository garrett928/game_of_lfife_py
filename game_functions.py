import sys
import pygame

from cell import Cell
from settings import Settings
import game_states as game_states

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
            game_states.set_mouse_dragging(True)
            print("mouse down")
        # if the mouse button is released than stop dragging
        if event.type == pygame.MOUSEBUTTONUP:
            print("mouse up")
            game_states.set_mouse_dragging(False)

    # if the mouse is being dragged than
    if game_states.get_mouse_dragging():
        mouse_pos = pygame.mouse.get_pos()
        cell_at_mouse_pos = (mouse_pos[0] // settings.cell_width,
                             mouse_pos[1] // settings.cell_height)
        # print("mouse pos: " + str(cell_at_mouse_pos))


def update_screen(screen: object, settings: object, cell_grid: Cell):
    """Update images on the screen and 'flip' to a new screen"""

    # draw the screens background
    screen.fill(settings.bg_color)

    if game_states.get_mouse_dragging():
        mouse_pos = pygame.mouse.get_pos()
        cell_at_mouse_pos = (mouse_pos[0] // settings.cell_width,
                             mouse_pos[1] // settings.cell_height)
        if cell_at_mouse_pos not in game_states.cell_dragging_list:
            cell_grid[cell_at_mouse_pos[0]][cell_at_mouse_pos[1]].change_on_drag()
            game_states.cell_dragging_list.append(cell_at_mouse_pos)

    # redraw the cells
    for col in cell_grid:
        for cell in col:
            cell.draw()
    # make the most recently drawn screen visible
    pygame.display.flip()
