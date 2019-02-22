import pygame
import settings
from cell import Cell
import game_functions as gf
from button import Button


def run_game():

    # Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.screen_title)

    # create a list of buttons on screen
    screen_buttons = []

    # create and initialize the grid of cells
    # grid is a 2d list of columns, or x pos
    # with each x pos being a list of cells with that x pos
    # cell_grid = [ [list_of_cells_at_x1], [list_of_cells_at_x2], [list_of_cells_at_x3]]
    cell_grid = []

    clear_button = Button(screen, settings.clr_btn_name,
                          settings.clr_btn_pos[0], settings.clr_btn_pos[1],
                          settings.clr_btn_pos[2], settings.clr_btn_pos[3])

    start_button = Button(screen, settings.start_btn_name, settings.start_btn_pos[0], settings.start_btn_pos[1],
                          settings.start_btn_pos[2], settings.start_btn_pos[3])

    screen_buttons.append(clear_button)
    screen_buttons.append(start_button)

    # init cells
    # use the screen and cell width and height to determine the number of cells on screen
    for x in range(0, settings.screen_width // settings.cell_width):
        x_list = []
        for y in range(0, settings.screen_height // settings.cell_height):
            cell = Cell(screen, x * settings.cell_width, y * settings.cell_height)
            x_list.append(cell)
        cell_grid.append(x_list)

    # start the game's main loop
    while True:
        # check pygame's events
        gf.check_events()
        # update the game's screen
        gf.update_screen(screen, cell_grid, screen_buttons)


run_game()
