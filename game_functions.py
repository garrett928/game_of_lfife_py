import sys
import pygame

from cell import Cell
import settings
import game_states as gs


def check_events():
    """Respond to keypresses and mouse events"""

    # watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        mouse_pos = pygame.mouse.get_pos()

        # if the mouse button is pushed
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is over the button when pressed
            if mouse_pos[0] < settings.clr_btn_pos[0] + settings.clr_btn_width and mouse_pos[0] > \
                    settings.clr_btn_pos[0] \
                    and mouse_pos[1] < settings.clr_btn_pos[1] + settings.clr_btn_pos[3] \
                    and mouse_pos[1] > settings.clr_btn_pos[1]:
                # set clr_btn_pressed
                gs.clr_btn_pressed = True
            elif mouse_pos[0] < settings.start_btn_pos[0] + settings.start_btn_width and mouse_pos[0] > \
                    settings.start_btn_pos[0] \
                    and mouse_pos[1] < settings.start_btn_pos[1] + settings.start_btn_pos[3] \
                    and mouse_pos[1] > settings.start_btn_pos[1]:
                # set clr_btn_pressed
                gs.start_btn_pressed = True
            elif not gs.is_running:
                gs.is_dragging = True
            print("mouse down")
        # if the mouse button is released than stop dragging
        if event.type == pygame.MOUSEBUTTONUP:
            print("mouse up")
            gs.set_mouse_dragging(False)


def update_screen(screen: object, cell_grid: Cell, screen_buttons):
    """Update images on the screen and 'flip' to a new screen"""

    # draw the screens background
    screen.fill(settings.bg_color)

    if gs.clr_btn_pressed:
        for col in cell_grid:
            for cell in col:
                cell.die()
        gs.clr_btn_pressed = False

    if gs.start_btn_pressed:
        if gs.is_running:
            gs.is_running = False
        else:
            gs.is_running = True
        gs.start_btn_pressed = False

    if gs.get_mouse_dragging():
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] % settings.cell_width > 3 or mouse_pos[1] % settings.cell_height > 3:
            cell_at_mouse_pos = (mouse_pos[0] // settings.cell_width,
                                 mouse_pos[1] // settings.cell_height)
            if cell_at_mouse_pos not in gs.cell_dragging_list:
                cell_grid[cell_at_mouse_pos[0]][cell_at_mouse_pos[1]].change_on_drag()
                gs.cell_dragging_list.append(cell_at_mouse_pos)

    if gs.is_running:
        for col in cell_grid:
            for cell in col:
                cell.birth()
    else:
        for col in cell_grid:
            for cell in col:
                cell.die()

    # redraw the cells
    for col in cell_grid:
        for cell in col:
            cell.draw()

    for button in screen_buttons:
        button.draw()
    # make the most recently drawn screen visible
    pygame.display.flip()
