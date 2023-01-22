from collections import deque

rows, cols = [int(x) for x in input().split()]
word = input()
snake_index = 0

for row in range(rows):
    result = deque()

    for col in range(cols):
        if snake_index == len(word):
            snake_index = 0
        if row % 2 == 0:
            result.append(word[snake_index])
        else:
            result.appendleft(word[snake_index])
        snake_index += 1
    print(''.join(result))