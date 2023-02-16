def check_valid_index(row_, col_):
    return 0 <= row_ < size and 0 <= col_ < size


def movement(row_, col_, direction_):
    return row_ + directions[direction_][0], col_ + directions[direction_][1]


def tunnel(player_row_, player_col_):
    for row in range(size):
        if "T" in matrix[row]:
            player_row_, player_col_ = row, matrix[row].index("T")
            matrix[player_row_][player_col_] = '.'
    return player_row_, player_col_


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size = int(input())
number = input()
matrix = [input().split() for _ in range(size)]
player_row, player_col, km = 0, 0, 0

while True:
    command = input()

    if command == 'End':
        print(f"Racing car {number} DNF.")
        break

    player_row, player_col = movement(player_row, player_col, command)
    km += 10

    if check_valid_index(player_row, player_col):
        step_on = matrix[player_row][player_col]

        if step_on == "T":
            km += 20
            matrix[player_row][player_col] = '.'
            player_row, player_col = tunnel(player_row, player_col)
            step_on = matrix[player_row][player_col]

        elif step_on == "F":
            matrix[player_row][player_col] = 'C'
            print(f"Racing car {number} finished the stage!")
            break

matrix[player_row][player_col] = 'C'

print(f'Distance covered {km} km.')
[print(*matrix[row], sep='') for row in range(size)]
