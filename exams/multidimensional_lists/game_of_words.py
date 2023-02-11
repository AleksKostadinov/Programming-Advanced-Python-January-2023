text = input()
size = int(input())
matrix = []
player_row, player_col = 0, 0
for row in range(size):
    matrix.append(list(input()))
    if "P" in matrix[row]:
        player_row = row
        player_col = matrix[row].index("P")

number_commands = int(input())
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for command in range(number_commands):
    direction = input()
    matrix[player_row][player_col] = '-'
    player_row += directions[direction][0]
    player_col += directions[direction][1]

    if not (0 <= player_row < size and 0 <= player_col < size):
        player_row -= directions[direction][0]
        player_col -= directions[direction][1]
        text = text[:-1]

    else:
        step_on = matrix[player_row][player_col]

        if step_on.isalpha():
            text += step_on
    matrix[player_row][player_col] = 'P'
print(text)
[print(*matrix[row], sep='') for row in range(size)]
