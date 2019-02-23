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
            # if the mouse is over the clear button when pressed
            if mouse_pos[0] < settings.clr_btn_pos[0] + settings.clr_btn_width and mouse_pos[0] > \
                    settings.clr_btn_pos[0] \
                    and mouse_pos[1] < settings.clr_btn_pos[1] + settings.clr_btn_pos[3] \
                    and mouse_pos[1] > settings.clr_btn_pos[1]:
                # set clr_btn_pressed
                gs.clr_btn_pressed = True
                # if the mouse is over the start button when pressed
            elif mouse_pos[0] < settings.start_btn_pos[0] + settings.start_btn_width and mouse_pos[0] > \
                    settings.start_btn_pos[0] \
                    and mouse_pos[1] < settings.start_btn_pos[1] + settings.start_btn_pos[3] \
                    and mouse_pos[1] > settings.start_btn_pos[1]:
                # set clear button's state
                gs.start_btn_pressed = True
            # if the game is not running and mouse is pressed, allow dragging
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

    # if the clear button has been pressed
    if gs.clr_btn_pressed:
        for col in cell_grid:
            for cell in col:
                # kill all the cells
                cell.die()
        # reset the clear buttons state
        gs.clr_btn_pressed = False

    # if the start button has been pressed
    if gs.start_btn_pressed:
        # start the game if not running
        if gs.is_running:
            gs.is_running = False
        # stop th game is it is running
        else:
            gs.is_running = True
        # reset the start button
        gs.start_btn_pressed = False

    # if the mouse is dragging
    if gs.get_mouse_dragging():
        # get the mouse position
        mouse_pos = pygame.mouse.get_pos()
        # if the mouse pos is "inside" a cell
        # uses '%' to make the mouse have to be inside the cell a bit
        # otherwise, as soon as the mouse touches a cell slightly it'd change states
        if mouse_pos[0] % settings.cell_width > 3 or mouse_pos[1] % settings.cell_height > 3:
            # get the pos of the mouse in "cell" coordinates by using floor division
            cell_at_mouse_pos = (mouse_pos[0] // settings.cell_width,
                                 mouse_pos[1] // settings.cell_height)
            # if a cell has not already been dragged across
            if cell_at_mouse_pos not in gs.cell_dragging_list:
                # change the state of the cell and add it to the list
                cell_grid[cell_at_mouse_pos[0]][cell_at_mouse_pos[1]].change_on_drag()
                gs.cell_dragging_list.append(cell_at_mouse_pos)

    x = 0
    # if the game is running
    if gs.is_running:
        for col in cell_grid:
            y = 0
            for cell in col:
                # var to count alive cells around given cell
                alive_neighbors = 0
                neighbor_pos = [x - 1, y - 1]
                if neighbor_pos[0] in range(0, settings.screen_width // settings.cell_width) \
                        and neighbor_pos[1] in range(0, settings.screen_height // settings.cell_height):
                    neighbor_cell = cell_grid[neighbor_pos[0]][neighbor_pos[1]]
                    if neighbor_cell.is_alive():
                        alive_neighbors += 1

                neighbor_pos = [x, y - 1]
                if neighbor_pos[0] in range(0, settings.screen_width // settings.cell_width) \
                        and neighbor_pos[1] in range(0, settings.screen_height // settings.cell_height):
                    neighbor_cell = cell_grid[neighbor_pos[0]][neighbor_pos[1]]
                    if neighbor_cell.is_alive():
                        alive_neighbors += 1

                neighbor_pos = [x + 1, y - 1]
                if neighbor_pos[0] in range(0, settings.screen_width // settings.cell_width) \
                        and neighbor_pos[1] in range(0, settings.screen_height // settings.cell_height):
                    neighbor_cell = cell_grid[neighbor_pos[0]][neighbor_pos[1]]
                    if neighbor_cell.is_alive():
                        alive_neighbors += 1

                neighbor_pos = [x, y - 1]
                if neighbor_pos[0] in range(0, settings.screen_width // settings.cell_width) \
                        and neighbor_pos[1] in range(0, settings.screen_height // settings.cell_height):
                    neighbor_cell = cell_grid[neighbor_pos[0]][neighbor_pos[1]]
                    if neighbor_cell.is_alive():
                        alive_neighbors += 1

                neighbor_pos = [x, y + 1]
                if neighbor_pos[0] in range(0, settings.screen_width // settings.cell_width) \
                        and neighbor_pos[1] in range(0, settings.screen_height // settings.cell_height):
                    neighbor_cell = cell_grid[neighbor_pos[0]][neighbor_pos[1]]
                    if neighbor_cell.is_alive():
                        alive_neighbors += 1

                neighbor_pos = [x - 1, y + 1]
                if neighbor_pos[0] in range(0, settings.screen_width // settings.cell_width) \
                        and neighbor_pos[1] in range(0, settings.screen_height // settings.cell_height):
                    neighbor_cell = cell_grid[neighbor_pos[0]][neighbor_pos[1]]
                    if neighbor_cell.is_alive():
                        alive_neighbors += 1

                neighbor_pos = [x, y + 1]
                if neighbor_pos[0] in range(0, settings.screen_width // settings.cell_width) \
                        and neighbor_pos[1] in range(0, settings.screen_height // settings.cell_height):
                    neighbor_cell = cell_grid[neighbor_pos[0]][neighbor_pos[1]]
                    if neighbor_cell.is_alive():
                        alive_neighbors += 1

                neighbor_pos = [x + 1, y + 1]
                if neighbor_pos[0] in range(0, settings.screen_width // settings.cell_width) \
                        and neighbor_pos[1] in range(0, settings.screen_height // settings.cell_height):
                    neighbor_cell = cell_grid[neighbor_pos[0]][neighbor_pos[1]]
                    if neighbor_cell.is_alive():
                        alive_neighbors += 1
                # print("cell coord: ( " + str(x) + ", " + str(y) + " )")
                if cell.is_alive():
                    if alive_neighbors <= 1:
                        cell.alive_next = False
                    elif alive_neighbors <= 3:
                        cell.alive_next = True
                    else:
                        cell.alive_next = False
                else:
                    if alive_neighbors == 3:
                        cell.alive_next = True

                y += 1
            x += 1

    # redraw the cells
    for col in cell_grid:
        for cell in col:
            if gs.is_running:
                if cell.alive_next:
                    cell.birth()
                else:
                    cell.die()
            cell.draw()
            cell.alive_next = False

    # redraw the buttons
    for button in screen_buttons:
        button.draw()

    # make the most recently drawn screen visible
    pygame.display.flip()
