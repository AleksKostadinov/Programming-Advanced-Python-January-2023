SIZE = 6
players = [{"name": x, "rest": False} for x in input().split(', ')]
matrix = [input().split() for x in range(SIZE)]

while True:
    player = players.pop(0)
    row, col = [int(x) for x in input()[1:-1].split(', ')]
    step_on = matrix[row][col]

    if player['rest']:
        player['rest'] = False
    elif step_on == 'E':
        print(f'{player["name"]} found the Exit and wins the game!')
        break
    elif step_on == 'T':
        print(f'{player["name"]} is out of the game! The winner is {players[0]["name"]}.')
        break
    elif step_on == 'W':
        print(f"{player['name']} hits a wall and needs to rest.")
        player['rest'] = True

    players.append(player)
