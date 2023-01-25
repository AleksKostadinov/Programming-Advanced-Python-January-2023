def check_valid(row, col):
    if 0 <= row < size and 0 <= col < size and matrix[row][col] != 'X':
        return True


def find_bunny():
    for row in range(size):
        if 'B' in matrix[row]:
            return row, matrix[row].index('B')


def movement_func():
    for direction, (row, col) in directions.items():
        bunny_move_row, bunny_move_col = row + bunny_row, col + bunny_col
        for jump in range(size):
            if check_valid(bunny_move_row, bunny_move_col):
                result[direction] = result.get(direction, 0) + matrix[bunny_move_row][bunny_move_col]
                bunny_move_row, bunny_move_col = row + bunny_move_row, col + bunny_move_col
            else:
                break


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

size = int(input())
matrix = [[int(x) if x[-1].isdigit() else x for x in input().split()] for _ in range(size)]
result = {}

bunny_row, bunny_col = find_bunny()
movement_func()
if sum(result.values()) != 0:
    max_direction = max(result, key=result.get)
    print(max_direction)
    for path in range(size):
        print_row, print_col = bunny_row + directions[max_direction][0], bunny_col + directions[max_direction][1]
        if check_valid(print_row, print_col):
            print(f"[{print_row}, {print_col}]")
            bunny_row, bunny_col = print_row, print_col
        else:
            break
    print(result[max_direction])
