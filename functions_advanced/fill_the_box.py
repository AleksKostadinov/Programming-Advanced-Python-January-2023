def fill_the_box(*args):
    height, length, width, *data = args
    volume = height * length * width
    no_free_space = 0

    for ele in data:
        if ele == 'Finish':
            break
        if volume - ele <= 0:
            ele -= volume
            volume = 0
        if volume > 0:
            volume -= ele
        else:
            no_free_space += ele

    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."

    return f"No more free space! You have {no_free_space} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))

