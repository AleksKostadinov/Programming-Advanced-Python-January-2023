def check_valid_index(row_, col_):
    return 0 <= row_ < rows and 0 <= col_ < cols and matrix[row_][col_] != "O"

def movement(row_, col_, direction_):
    return row_ + directions[direction_][0], col_ + directions[direction_][1]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

rows, cols = [int(x) for x in input().split()]
matrix = []
player_row, player_col = 0, 0
opponents, moves_count = 0, 0

for row in range(rows):
    matrix.append(input().split())
    if "B" in matrix[row]:
        player_row, player_col = row, matrix[row].index("B")
        matrix[player_row][player_col] = '-'
        break

while True:
    command = input()
    if command == 'Finish':
        break

    source_row, source_col = player_row, player_col
    player_row, player_col = movement(player_row, player_col, command)

    if check_valid_index(player_row, player_col):
        step_on = matrix[player_row][player_col]

        if step_on == "P":
            matrix[player_row][player_col] = '-'
            opponents += 1
            moves_count += 1
        elif step_on == "-":
            moves_count += 1
    else:
        player_row, player_col = source_row, source_col

    if opponents == 3:
        break

print(f"Game over!\nTouched opponents: {opponents} Moves made: {moves_count}")
