class Settings:
    """A class to store all settings for 'Game Of Life'"""

    def __init__(self):
        """Initialize game settings"""

        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.cell_width = 10
        self.cell_height = 10
        self.bg_color = (255, 255, 255)
        self.screen_title = "Game of Life"
