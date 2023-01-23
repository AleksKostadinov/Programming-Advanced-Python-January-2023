from collections import deque


def player_position(matrix, rows_number, columns_number):
    player_coordinates = ()
    for row in range(rows_number):
        for column in range(columns_number):
            if matrix[row][column] == "P":
                player_coordinates = (row, column)
                break
    return player_coordinates


def bunnies_position(matrix, rows_number, columns_number):
    bunnies_coordinates = []
    for row in range(rows_number):
        for column in range(columns_number):
            if matrix[row][column] == "B":
                bunnies_coordinates.append([row, column])
    return bunnies_coordinates


def not_in_matrix(row, column, rows_number, columns_number):
    return row < 0 or column < 0 or row >= rows_number or column >= columns_number


def get_children(row, column, rows_number, columns_number):
    children = []
    possible_children = [
        [row - 1, column],
        [row, column - 1],
        [row, column + 1],
        [row + 1, column]
    ]
    for child_row, child_column in possible_children:
        if not_in_matrix(child_row, child_column, rows_number, columns_number):
            continue
        else:
            children.append([child_row, child_column])
    return children


def move(direction: str, row, column):
    if direction == "L":
        column -= 1
    elif direction == "R":
        column += 1
    elif direction == "U":
        row -= 1
    elif direction == "D":
        row += 1
    return (row, column)


def spawn_bunnies(bunnies):
    new_bunnies = []
    for bunnie_row, bunnie_column in bunnies:
        children = get_children(bunnie_row, bunnie_column, row_count, column_count)
        for child in children:
            new_bunnies.append(child)
    return new_bunnies


row_count, column_count = [int(i) for i in input().split()]
matrix = [list(input()) for row in range(row_count)]
commands = deque(input())
won = False
dead = False
player_row, player_column = player_position(matrix, row_count, column_count)
bunnies = bunnies_position(matrix, row_count, column_count)

while not won and not dead:
    command = commands.popleft()

    new_player_row, new_player_column = move(command, player_row, player_column)
    matrix[player_row][player_column] = "."
    won = not_in_matrix(new_player_row, new_player_column, row_count, column_count)

    if not won:
        player_row, player_column = new_player_row, new_player_column
        if matrix[player_row][player_column] == "B":
            dead = True
        else:
            matrix[player_row][player_column] = "P"

    bunnies = spawn_bunnies(bunnies)
    for bunnie_row, bunnie_column in bunnies:
        matrix[bunnie_row][bunnie_column] = "B"

    if matrix[player_row][player_column] == "B" and not won:
        dead = True

for row in matrix:
    print(*row, sep="")

if won:
    print(f"won: {player_row} {player_column}")
elif dead:
    print(f"dead: {player_row} {player_column}")

# https://github.com/mabrasheva/SoftUni-Python-Advanced/blob/main/Multidimensional_Lists/radioactive_mutate_vampire_bunnies.py
