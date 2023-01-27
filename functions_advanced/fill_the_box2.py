def fill_the_box(height, length, width, *args):
    volume = height * width * length
    no_free_space = 0

    for ele in args:
        if ele == 'Finish':
            break

        if volume > 0:
            if ele <= volume:
                volume -= ele
            else:
                no_free_space += ele - volume
                volume = 0
        else:
            no_free_space += ele

    if volume:
        return f"There is free space in the box. You could put {volume} more cubes."
    return f"No more free space! You have {no_free_space} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
