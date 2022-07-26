# 15/15

def is_in_board(coordinate):
    counter = 0
    # bottom right
    if coordinate[0] + 1 <= 8 and coordinate[1] - 2 >= 1:
        print("bottom right")
        counter += 1
    # mid right 1
    if coordinate[0] + 2 <= 8 and coordinate[1] - 1 <= 8:
        print("mid right 1")
        counter += 1
    # mid right 2
    if coordinate[0] + 2 <= 8 and coordinate[1] + 1 >= 1:
        counter += 1
        print("mid right 2")
    # top right
    if coordinate[0] + 1 <= 8 and coordinate[1] + 2 <= 8:
        counter += 1
        print("top right")
    # bottom_left
    if coordinate[0] - 1 >= 1 and coordinate[1] - 2 >= 1:
        counter += 1
        print("bottom left")
    # mid_left_1
    if coordinate[0] - 2 >= 1 and coordinate[1] - 1 >= 1:
        counter += 1
        print("mid left 1")
    # mid_left_2
    if coordinate[0] - 2 >= 1 and coordinate[1] + 1 <= 8:
        counter += 1
        print("mid left 2")
    # top_left
    if coordinate[0] - 1 >= 1 and coordinate[1] + 2 <= 8:
        counter += 1
        print("top left")
    return counter


def knight_jumps(str_param):
    str_param = str_param.strip("(").strip(")")
    x = int(str_param.split()[0])
    y = int(str_param.split()[1])
    coordinate = [x, y]
    result = is_in_board(coordinate)
    return result


print(knight_jumps("(3 7)"))
