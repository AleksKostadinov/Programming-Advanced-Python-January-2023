from collections import deque


class WaterDispenser:
    queue = deque()
    quantity_water = 0

    def add_to_queue(self, name: str):
        self.queue.append(name)

    def refill(self, liters_: int):
        self.quantity_water += liters_

    def get_water(self, liters_: int):
        if self.quantity_water >= liters_:
            self.quantity_water -= liters_
            return f"{self.queue.popleft()} got water"
        return f'{self.queue.popleft()} must wait'


COMMAND_START = 'Start'
COMMAND_END = 'End'
COMMAND_REFILL = 'refill'

dispenser = WaterDispenser()
dispenser.quantity_water = int(input())
person = input()

while person != COMMAND_START:
    dispenser.add_to_queue(person)
    person = input()

command = input()
while command != COMMAND_END:
    if command.startswith(COMMAND_REFILL):
        _, liters = command.split()
        dispenser.refill(int(liters))
    else:
        print(dispenser.get_water(int(command)))
    command = input()

print(f'{dispenser.quantity_water} liters left')