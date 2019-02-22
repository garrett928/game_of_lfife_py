# screen settings
screen_width = 800
screen_height = 600

bg_color = (150, 150, 150)
screen_title = "Game of Life"

cell_width = 10
cell_height = 10

clr_btn_width = 60
clr_btn_height = 25
clr_btn_padding = 10

start_btn_width = 60
start_btn_height = 25
start_btn_padding = 10

# create clear button
clr_btn_pos = (screen_width - clr_btn_width - clr_btn_padding,
               0 + clr_btn_padding,
               clr_btn_width, clr_btn_height)

start_btn_pos = (screen_width - clr_btn_width - clr_btn_padding - start_btn_width - start_btn_padding,
                 0 + start_btn_padding, start_btn_width, start_btn_height)

clr_btn_name = "clear button"
clr_btn_text = "Clear"

start_btn_name = "start button"
start_button_text = "Start"
