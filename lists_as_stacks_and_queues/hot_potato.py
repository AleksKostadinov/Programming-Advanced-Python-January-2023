from _collections import deque

players = input().split()
toss = int(input())

players_deque = deque(players)
counter = 0

while len(players_deque) > 1:
    counter += 1
    current_player = players_deque.popleft()

    if counter == toss:
        print(f'Removed {current_player}')
        counter = 0
    else:
        players_deque.append(current_player)

print(f'Last is {players_deque[0]}')
