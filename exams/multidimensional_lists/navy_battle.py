def check_valid_index(row_, col_):
    return 0 <= row_ < size and 0 <= col_ < size


def movement(row_, col_, direction_):
    return row_ + directions[direction_][0], col_ + directions[direction_][1]


size = int(input())
matrix = []
submarine_row, submarine_col, mine_blown, cruiser_destroyed = 0, 0, 0, 0
submarine_is_destroyed, cruisers_are_destroyed = False, False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(list(input()))
    if "S" in matrix[row]:
        submarine_row, submarine_col = row, matrix[row].index("S")
        matrix[submarine_row][submarine_col] = "-"

while not submarine_is_destroyed and not cruisers_are_destroyed:
    command = input()
    submarine_row, submarine_col = movement(submarine_row, submarine_col, command)

    if check_valid_index(submarine_row, submarine_col):
        step_on = matrix[submarine_row][submarine_col]

        if step_on == "*":
            matrix[submarine_row][submarine_col] = "-"
            mine_blown += 1
            if mine_blown == 3:
                matrix[submarine_row][submarine_col] = "S"
                submarine_is_destroyed = True
        elif step_on == "C":
            matrix[submarine_row][submarine_col] = "-"
            cruiser_destroyed += 1
            if cruiser_destroyed == 3:
                matrix[submarine_row][submarine_col] = "S"
                cruisers_are_destroyed = True

if submarine_is_destroyed:
    print(f'Mission failed, U-9 disappeared! Last known coordinates {[submarine_row, submarine_col]}!')

if cruisers_are_destroyed:
    print(f'Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')

[print(*matrix[row], sep='') for row in range(size)]
