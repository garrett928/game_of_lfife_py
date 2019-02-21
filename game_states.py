is_dragging = False


def get_mouse_dragging():
    return is_dragging


def set_mouse_dragging(dragging):
    global is_dragging
    is_dragging = dragging
