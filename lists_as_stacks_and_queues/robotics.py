from datetime import datetime, timedelta
from collections import deque

robots_list = input().split(';')
robots = {}

for robot in robots_list:
    name, work_time = robot.split('-')
    robots[name] = [int(work_time), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()
    free_robots = []

    for key, value in robots.items():
        if value[1] != 0:
            robots[key][1] -= 1

    for key, value in robots.items():
        if value[1] == 0:
            free_robots.append([key, value])

    if not free_robots:
        products.append(product)
        continue

    robot_name, data = free_robots[0]
    robots[robot_name][1] = data[0]

    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")


