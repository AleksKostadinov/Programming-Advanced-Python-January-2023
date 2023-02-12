def check_valid_index(row_, col_):
    return 0 <= row_ < size and 0 <= col_ < size


def out_destination(player_row_, player_col_):
    if player_row_ < 0:
        player_row_ = size - 1
    elif player_row_ == size:
        player_row_ = 0
    elif player_col_ < 0:
        player_col_ = size - 1
    elif player_col_ == size:
        player_col_ = 0
    return player_row_, player_col_


def movement(row_, col_, direction_):
    return row_ + directions[direction_][0], col_ + directions[direction_][1]


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size = int(input())
player_row, player_col, collected_coins = 0, 0, 0
player_path = []

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]

for row in range(len(matrix)):
    if "P" in matrix[row]:
        player_row, player_col = row, matrix[row].index("P")
        matrix[player_row][player_col] = 0
        player_path.append([player_row, player_col])

while collected_coins < 100:
    command = input()
    player_row, player_col = movement(player_row, player_col, command)
    player_row, player_col = out_destination(player_row, player_col)

    if check_valid_index(player_row, player_col):
        step_on = matrix[player_row][player_col]
        player_path.append([player_row, player_col])
        if step_on == "X":
            collected_coins /= 2
            break
        else:
            collected_coins += matrix[player_row][player_col]
            matrix[player_row][player_col] = 0

if collected_coins >= 100:
    print(f'You won! You\'ve collected {int(collected_coins)} coins.')
else:
    print(f'Game over! You\'ve collected {int(collected_coins)} coins.')
print('Your path:')

for row in player_path:
    print(f'{row}')
