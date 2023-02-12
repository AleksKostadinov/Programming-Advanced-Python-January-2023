def check_valid_index(row_, col_):
    return 0 <= row_ < size and 0 <= col_ < size


def movement(row_, col_, direction_):
    return row_ + directions[direction_][0], col_ + directions[direction_][1]


def find_tunnel(player_row_, player_col_):
    for row_ in range(size):
        for col in range(size):
            if 'T' in matrix[row_]:
                player_row_ = row_
                player_col_ = matrix[row_].index("T")
                matrix[player_row_][player_col_] = '.'
    return player_row_, player_col_


size = int(input())
racing_number = input()
matrix = [input().split() for row in range(size)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

player_row, player_col, tunnel_row, tunnel_col, km_passed = 0, 0, 0, 0, 0
finished = False

while True:
    command = input()

    if command == 'End':
        matrix[player_row][player_col] = 'C'
        break

    player_row, player_col = movement(player_row, player_col, command)
    km_passed += 10

    if check_valid_index(player_row, player_col):
        step_on = matrix[player_row][player_col]

        if step_on == 'T':
            player_row, player_col = find_tunnel(player_row, player_col)
            matrix[player_row][player_col] = '.'
            km_passed += 20

        elif step_on == 'F':
            matrix[player_row][player_col] = 'C'
            finished = True
            break

if finished:
    print(f'Racing car {racing_number} finished the stage!')
else:
    print(f'Racing car {racing_number} DNF.')

print(f'Distance covered {km_passed} km.')
[print(*matrix[row], sep='') for row in range(size)]
