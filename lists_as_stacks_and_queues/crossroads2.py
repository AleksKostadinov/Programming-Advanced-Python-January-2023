from collections import deque

green_window = int(input())
free_window = int(input())
command = input()
crash = False
cars = deque()
passed_cars = 0

while command != 'END':
    if command == 'green':
        current_time = green_window
        if cars:
            while current_time > 0 and cars:
                car = cars.popleft()
                if current_time + free_window < len(car):
                    crash_char = car[current_time + free_window]
                    print(f"A crash happened!\n{car} was hit at {crash_char}.")
                    crash = True
                    break
                else:
                    current_time -= len(car)
                    passed_cars += 1
        if crash:
            break
    else:
        cars.append(command)
    command = input()

if not crash:
    print(f"Everyone is safe.\n{passed_cars} total cars passed the crossroads.")
