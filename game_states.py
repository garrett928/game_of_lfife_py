is_dragging = False
clr_btn_pressed = False
start_btn_pressed = False
is_running = False
cell_dragging_list = []


def get_mouse_dragging():
    return is_dragging


def set_mouse_dragging(dragging):
    global is_dragging
    is_dragging = dragging
    if not is_dragging:
        cell_dragging_list.clear()
