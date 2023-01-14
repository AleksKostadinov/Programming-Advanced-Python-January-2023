from collections import deque

gas_stations = int(input())
pumps_data = deque()

for _ in range(gas_stations):
    info = [int(x) for x in input().split()]
    pumps_data.append(info)

pumps_data_copy = pumps_data.copy()
index = 0
tank = 0

while pumps_data_copy:
    fuel, distance = pumps_data_copy.popleft()
    tank += fuel

    if tank < distance:
        pumps_data.rotate(-1)  # same as: pumps_data.append(pumps_data.popleft())
        pumps_data_copy = pumps_data.copy()
        index += 1
        tank = 0
    else:
        tank -= distance

print(index)
