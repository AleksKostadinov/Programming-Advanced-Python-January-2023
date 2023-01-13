from collections import deque

queue = deque()

while True:
    names = input()

    if names == 'End':
        print(f'{len(queue)} people remaining.')
        break
    elif names == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(names)
