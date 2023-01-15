from collections import deque

green_window = int(input())
free_window = int(input())
command = input()

cars = deque()
total_cars = 0

while command != 'END':
    if command != 'green':
        cars.append(command)
    else:
        current_green = green_window
        while cars and current_green > 0:
            car = cars.popleft()
            time = current_green + free_window

            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                raise SystemExit
            current_green -= len(car)
            total_cars += 1
    command = input()

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads.")
