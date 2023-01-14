from collections import deque

gas_stations = int(input())
pumps = deque()

for _ in range(gas_stations):
    info = [int(x) for x in input().split()]
    pumps.append(info)

for attempt in range(gas_stations):
    tank = 0
    full_circle = True
    for fuel, distance in pumps:
        tank += fuel
        if tank >= distance:
            tank -= distance
        else:
            full_circle = False
            break
    if full_circle:
        print(attempt)
        break
    else:
        pumps.append(pumps.popleft())
