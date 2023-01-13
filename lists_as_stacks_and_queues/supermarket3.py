from collections import deque

queue = deque()
COMMAND_END = 'End'
COMMAND_PAID = 'Paid'

while True:
    names = input()

    if names == COMMAND_END:
        print(f'{len(queue)} people remaining.')
        break
    elif names == COMMAND_PAID:
        while queue:
            print(queue.popleft())
    else:
        queue.append(names)
