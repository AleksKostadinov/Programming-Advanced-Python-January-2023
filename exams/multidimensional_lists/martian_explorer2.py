from collections import deque

def check_valid_index(row_, col_):
    return 0 <= row_ < size and 0 <= col_ < size

def movement(row_, col_, direction_):
    return row_ + directions[direction_][0], col_ + directions[direction_][1]

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

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

player_row, player_col, matrix = 0, 0, []
water, metal, concrete = 0, 0, 0
size = 6

for row in range(size):
    matrix.append(input().split())
    if "E" in matrix[row]:
        player_row, player_col = row, matrix[row].index("E")

command_list = deque(input().split(', '))
while command_list:
    command = command_list.popleft()
    player_row, player_col = movement(player_row, player_col, command)

    player_row, player_col = out_destination(player_row, player_col)

    if check_valid_index(player_row, player_col):
        step_on = matrix[player_row][player_col]

        if step_on == "R":
            print(f'Rover got broken at ({player_row}, {player_col})')
            break
        elif step_on == "C":
            concrete += 1
            print(f'Concrete deposit found at ({player_row}, {player_col})')
        elif step_on == "W":
            water += 1
            print(f'Water deposit found at ({player_row}, {player_col})')
        elif step_on == "M":
            metal += 1
            print(f'Metal deposit found at ({player_row}, {player_col})')

if all([water, metal, concrete]):
    print(f'Area suitable to start the colony.')
else:
    print("Area not suitable to start the colony.")