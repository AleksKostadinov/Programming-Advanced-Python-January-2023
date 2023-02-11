def check_valid_index(row_, col_):
    return 0 <= row_ < SIZE and 0 <= col_ < SIZE


def movement(row_, col_, direction_):
    return row_ + directions[direction_][0], col_ + directions[direction_][1]


SIZE = 8
matrix = []
king_row, king_col, queen_pos = 0, 0, []

for row in range(SIZE):
    matrix.append(input().split())
    if "K" in matrix[row]:
        king_row = row
        king_col = matrix[row].index("K")

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'top_left': (-1, -1),
    'top_right': (-1, 1),
    'bottom_left': (1, -1),
    'bottom_right': (1, 1),
}

for direction in directions:
    new_row, new_col = king_row, king_col
    for step in range(SIZE):
        new_row, new_col = movement(new_row, new_col, direction)
        if check_valid_index(new_row, new_col):
            if matrix[new_row][new_col] == 'Q':
                queen_pos.append([new_row, new_col])
                break
        else:
            break
if queen_pos:
    [print(row) for row in queen_pos]
else:
    print("The king is safe!")
