def movement(row_, col_, direction_):
    return row_ + directions[direction_][0], col_ + directions[direction_][1]


def out_destination(player_row_, player_col_):
    return player_row_ < 0 or player_row_ == size or player_col_ < 0 or player_col_ == size


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size, matrix = int(input()), []
player_row, player_col, tea, collected_tea, game_lost = 0, 0, 0, False, False

for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        player_row, player_col = row, matrix[row].index("A")
        matrix[player_row][player_col] = '*'

while True:
    command = input()
    player_row, player_col = movement(player_row, player_col, command)

    if out_destination(player_row, player_col):
        game_lost = True
        break

    step_on = matrix[player_row][player_col]

    if step_on.isdigit():
        tea += int(step_on)
    elif step_on == "R":
        game_lost = True
        matrix[player_row][player_col] = '*'
        break

    matrix[player_row][player_col] = '*'
    if tea >= 10:
        collected_tea = True
        break

if game_lost:
    print("Alice didn't make it to the tea party.")
if collected_tea:
    print("She did it! She went to the party.")
[print(*matrix[row], sep=' ') for row in range(size)]
