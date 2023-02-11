def check_valid_index(row_, col_):
    return 0 <= row_ < size and 0 <= col_ < size


def movement(row_, col_, direction_):
    return row_ + directions[direction_][0], col_ + directions[direction_][1]


def find_burrow(player_row, player_col):
    for row in range(size):
        for col in range(size):
            if 'B' in matrix[row]:
                player_row = row
                player_col = matrix[row].index("B")
                matrix[player_row][player_col] = '.'
    return player_row, player_col


size = int(input())
matrix = []
player_row, player_col, food = 0, 0, 0
goes_out = False
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(list(input()))
    if "S" in matrix[row]:
        player_row = row
        player_col = matrix[row].index("S")
        matrix[player_row][player_col] = '.'

while not goes_out and food < 10:  # 1)commands

    command = input()
    # player_row += directions[command][0]
    # player_col += directions[command][1]

    player_row, player_col = movement(player_row, player_col, command)
    if not check_valid_index(player_row, player_col):
        goes_out = True
        break

    step_on = matrix[player_row][player_col]

    if step_on == "*":
        food += 1

    elif step_on == 'B':
        player_row, player_col = find_burrow(player_row, player_col)

    matrix[player_row][player_col] = '.'
if check_valid_index(player_row, player_col): # 
    matrix[player_row][player_col] = 'S'

if goes_out:
    print("Game over!")
if food >= 10:
    print('You won! You fed the snake.')

print(f'Food eaten: {food}')
[print(*matrix[row], sep='') for row in range(size)]
