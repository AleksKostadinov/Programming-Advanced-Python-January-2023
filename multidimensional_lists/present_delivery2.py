# https://github.com/mabrasheva/SoftUni-Python-Advanced/blob/main/Multidimensional_Lists/present_delivery.py
def find_santa(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == "S":
                return row, column


def count_nice_kids(matrix):
    nice_kids_count = 0
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == "V":
                nice_kids_count += 1
    return nice_kids_count


def move(row, column, direction):
    if direction == "up":
        return row - 1, column
    elif direction == "down":
        return row + 1, column
    elif direction == "right":
        return row, column + 1
    elif direction == "left":
        return row, column - 1


def valid_coordinates(row, column, size):
    return 0 <= row < size and 0 <= column < size


def get_around_cells(row, column, matrix):
    around_cells = []
    possible_cells = [
        [row - 1, column],
        [row + 1, column],
        [row, column + 1],
        [row, column - 1],
    ]
    for child_row, child_column in possible_cells:
        if valid_coordinates(child_row, child_column, len(matrix)):
            around_cells.append([child_row, child_column])
    return around_cells


def check_house(santa_row, santa_column, matrix, presents, happy_nice_kids):
    if matrix[santa_row][santa_column] == "V":
        presents -= 1
        happy_nice_kids += 1
    elif matrix[santa_row][santa_column] == "C":
        around_cells = get_around_cells(santa_row, santa_column, matrix)
        for row, column in around_cells:
            if matrix[row][column] == "V":
                happy_nice_kids += 1
                presents -= 1
            elif matrix[row][column] == "X":
                presents -= 1
            matrix[row][column] = "-"
    matrix[santa_row][santa_column] = "S"
    return presents, happy_nice_kids


presents_count = int(input())
size_matrix = int(input())

matrix = [list(input().split()) for row in range(size_matrix)]
santa_row, santa_column = find_santa(matrix)
nice_kids_count = count_nice_kids(matrix)
happy_nice_kids = 0

while presents_count:
    command = input()
    if command == "Christmas morning":
        break
    matrix[santa_row][santa_column] = "-"
    santa_row, santa_column = move(santa_row, santa_column, command)
    presents_count, happy_nice_kids = check_house(santa_row, santa_column, matrix, presents_count, happy_nice_kids)

if presents_count == 0 and happy_nice_kids != nice_kids_count:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row)
if nice_kids_count == happy_nice_kids:
    print(f"Good job, Santa! {happy_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count - happy_nice_kids} nice kid/s.")