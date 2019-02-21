import pygame
from settings import Settings
from cell import Cell
import game_functions as gf


def run_game():

    # create settings object
    settings = Settings()

    # Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.screen_title)

    cell_grid = []
    y_list = []
    # init cells
    num_cols = settings.screen_width / settings.cell_width
    num_rows = settings.screen_height / settings.cell_height
    # create a vertical row

    for y in range(0, 60):
        cell = Cell(screen, 0, y * settings.cell_height)
        y_list.append(cell)

    cell_grid.append(y_list)

    # start the game's main loop
    while True:
        # check pygame's events
        gf.check_events()
        # update the game's screen
        gf.upadte_screen(screen, settings, cell_grid)



run_game()
