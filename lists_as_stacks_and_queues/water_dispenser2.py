from collections import deque


def add_names_to_queue():
    queue = deque()
    while True:
        command = input()
        if command == COMMAND_START:
            break
        queue.append(command)
    return queue


COMMAND_START = 'Start'
COMMAND_END = 'End'
COMMAND_REFILL = 'refill'

quantity_water = int(input())
queue = add_names_to_queue()

while True:
    command = input()
    if command == COMMAND_END:
        print(f'{quantity_water} liters left')
        break
    elif command.startswith(COMMAND_REFILL):
        litters = int(command.split()[-1])
        quantity_water += litters
    else:
        litters = int(command)
        if quantity_water >= litters:
            print(f"{queue.popleft()} got water")
            quantity_water -= litters
        else:
            print(f'{queue.popleft()} must wait')
