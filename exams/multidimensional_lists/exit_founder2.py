from collections import deque

SIZE = 6
players = input().split(', ')
matrix = [input().split() for _ in range(SIZE)]
walled = deque()
while True:
    player_row, player_col = [int(x) for x in input()[1:-1].split(', ')]
    step_on = matrix[player_row][player_col]

    if players[0] in walled:
        walled.popleft()
    elif step_on == "E":
        print(f"{players[0]} found the Exit and wins the game!")
        break
    elif step_on == "T":
        print(f"{players[0]} is out of the game! The winner is {players[1]}.")
        break
    elif step_on == 'W':
        print(f'{players[0]} hits a wall and needs to rest.')
        walled.append(players[0])

    players[0], players[1] = players[1], players[0]
