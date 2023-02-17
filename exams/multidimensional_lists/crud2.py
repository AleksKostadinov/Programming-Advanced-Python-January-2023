def movement(row_, col_, direction_):
    return row_ + directions[direction_][0], col_ + directions[direction_][1]


SIZE = 6
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(SIZE)]
player_row, player_col = [int(x) for x in input()[1:-1].split(', ')]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
command = input()

while command != 'Stop':
    action, direction, *symbol = command.split(', ')
    player_row, player_col = movement(player_row, player_col, direction)
    step_on = matrix[player_row][player_col]

    if action == 'Create':
        if step_on == '.':
            matrix[player_row][player_col] = symbol[0]
    elif action == 'Update':
        if not step_on == '.':
            matrix[player_row][player_col] = symbol[0]
    elif action == 'Delete':
        if not step_on == '.':
            matrix[player_row][player_col] = '.'
    elif action == 'Read':
        if not step_on == '.':
            print(f'{matrix[player_row][player_col]}')

    command = input()

[print(*matrix[row], sep=' ') for row in range(SIZE)]
