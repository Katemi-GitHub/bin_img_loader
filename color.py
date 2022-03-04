def get_color_4bit(bin_col=int):
    if bin_col == 0:
        color = 0, 0, 0
    elif bin_col == 1:
        color = 0, 0, 170
    elif bin_col == 2:
        color = 0, 170, 0
    elif bin_col == 3:
        color = 0, 170, 170
    elif bin_col == 4:
        color = 170, 0, 0
    elif bin_col == 5:
        color = 170, 0, 170
    elif bin_col == 6:
        color = 170, 85, 0
    elif bin_col == 7:
        color = 170, 170, 170
    elif bin_col == 8:
        color = 85, 85, 85
    elif bin_col == 9:
        color = 85, 85, 255
    elif bin_col == 10:
        color = 85, 255, 85
    elif bin_col == 11:
        color = 85, 255, 255
    elif bin_col == 12:
        color = 255, 85, 85
    elif bin_col == 13:
        color = 255, 85, 255
    elif bin_col == 14:
        color = 255, 255, 85
    elif bin_col == 15:
        color = 255, 255, 255
    return color

def get_color_5bit(bin_color=int):
    if bin_color == 0:
        color = 0, 0, 0
    elif bin_color == 1:
        color = 0, 0, 170
    elif bin_color == 2:
        color = 85, 0, 0
    elif bin_color == 3:
        color = 85, 0, 170
    elif bin_color == 4:
        color = 170, 0, 0
    elif bin_color == 5:
        color = 170, 0, 170
    elif bin_color == 6:
        color = 255, 0, 0
    elif bin_color == 7:
        color = 255, 0, 170
    elif bin_color == 8:
        color = 0, 85, 0
    elif bin_color == 9:
        color = 0, 85, 170
    elif bin_color == 10:
        color = 85, 85, 0
    elif bin_color == 11:
        color = 85, 85, 170
    elif bin_color == 12:
        color = 170, 85, 0
    elif bin_color == 13:
        color = 170, 85, 170
    elif bin_color == 14:
        color = 255, 85, 0
    elif bin_color == 15:
        color = 255, 85, 170
    elif bin_color == 16:
        color = 0, 170, 0
    elif bin_color == 17:
        color = 0, 170, 170
    elif bin_color == 18:
        color = 85, 170, 0
    elif bin_color == 19:
        color = 85, 170, 170
    elif bin_color == 20:
        color = 170, 170, 0
    elif bin_color == 21:
        color = 170, 170, 170
    elif bin_color == 22:
        color = 255, 170, 0
    elif bin_color == 23:
        color = 255, 170, 170
    elif bin_color == 24:
        color = 0, 255, 0
    elif bin_color == 25:
        color = 0, 255, 170
    elif bin_color == 26:
        color = 85, 255, 0
    elif bin_color == 27:
        color = 85, 255, 170
    elif bin_color == 28:
        color = 170, 255, 0
    elif bin_color == 29:
        color = 170, 255, 170
    elif bin_color == 30:
        color = 255, 255, 0
    elif bin_color == 31:
        color = 255, 255, 170
    return color
