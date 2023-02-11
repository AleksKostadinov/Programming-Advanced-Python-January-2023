def check_valid_index(row_, col_):
    return 0 <= row_ < size and 0 <= col_ < size


def movement(row_, col_, direction_):
    return row_ + directions[direction_][0], col_ + directions[direction_][1]


size = int(input())
bombs_number = int(input())
matrix = [['0' for x in range(size)] for row in range(size)]

for bomb in range(bombs_number):
    row, col = [int(x) for x in input()[1:-1].split(', ')]
    matrix[row][col] = '*'

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

for row in range(size):
    for col in range(size):
        digit_row, digit_col = row, col
        if matrix[row][col] != '*':
            count = 0
            for direction in directions:
                digit_row, digit_col = movement(row, col, direction)
                if check_valid_index(digit_row, digit_col) and matrix[digit_row][digit_col] == '*':
                    count += 1
                    matrix[row][col] = str(count)

[print(*matrix[row], sep=' ') for row in range(size)]
