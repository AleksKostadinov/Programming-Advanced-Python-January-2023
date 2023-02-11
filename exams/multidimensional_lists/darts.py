def check_valid_index(row_, col_):
    return 0 <= row_ < SIZE and 0 <= col_ < SIZE


def bonus(row_, col_):
    return int(matrix[0][col_]) + int(matrix[SIZE - 1][col_]) + int(matrix[row_][0]) + int(matrix[row_][SIZE - 1])


SIZE = 7
players = [{"name": x, "SCORE": 501, "throws": 0} for x in input().split(', ')]
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(SIZE)]

while True:
    player = players.pop(0)
    row, col = [int(x) for x in input()[1:-1].split(', ')]
    step_on = str(matrix[row][col])
    player['throws'] += 1
    if not check_valid_index(row, col):
        continue

    if step_on.isdigit():
        player['SCORE'] -= int(step_on)
    elif step_on == 'D':
        player['SCORE'] -= 2 * bonus(row, col)
    elif step_on == 'T':
        player['SCORE'] -= 3 * bonus(row, col)
    elif step_on == 'B':
        break

    if player['SCORE'] <= 0:
        break

    players.append(player)

print(f"{player['name']} won the game with {player['throws']} throws!")
