rows, cols = [int(x) for x in input().split(', ')]
matrix = []
player_row, player_col, decorations, gifts, cookies = 0, 0, 0, 0, 0
items = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
for row in range(rows):
    matrix.append(input().split())
    if "Y" in matrix[row]:
        player_row, player_col = row, matrix[row].index("Y")

    if "D" in matrix[row] or "G" in matrix[row] or "C" in matrix[row]:
        items += matrix[row].count("D") + matrix[row].count("G") + matrix[row].count("C")

command = input()

while command != 'End' and items:
    direction, steps = [int(x) if x.isdigit() else x for x in command.split('-')]
    matrix[player_row][player_col] = 'x'
    for step in range(steps):
        player_row += directions[direction][0]
        player_col += directions[direction][1]

        if player_row < 0:
            player_row = rows - 1
        elif player_row == rows:
            player_row = 0
        elif player_col < 0:
            player_col = cols - 1
        elif player_col == cols:
            player_col = 0

        step_on = matrix[player_row][player_col]

        if step_on == 'D':
            decorations += 1
            items -= 1
        elif step_on == 'G':
            gifts += 1
            items -= 1
        elif step_on == 'C':
            cookies += 1
            items -= 1
        matrix[player_row][player_col] = 'x'
        if not items:
            break
    matrix[player_row][player_col] = 'Y'
    if not items:
        break

    command = input()
if not items:
    print("Merry Christmas!")

print(f"You've collected:\n- {decorations} Christmas decorations\n- {gifts} Gifts\n- {cookies} Cookies")

[print(*matrix[row]) for row in range(rows)]

