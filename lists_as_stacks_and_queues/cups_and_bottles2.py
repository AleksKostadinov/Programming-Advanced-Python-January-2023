from collections import deque

cup_capacity = deque([int(x) for x in input().split()])
bottle_capacity = list(map(int, input().split()))

wasted_water = 0

while cup_capacity and bottle_capacity:
    bottle = bottle_capacity.pop()
    cup = cup_capacity.popleft()

    if bottle >= cup:
        bottle -= cup
        wasted_water += bottle
    else:
        cup -= bottle
        cup_capacity.appendleft(cup)

if cup_capacity:
    print(f"Cups: {' '.join(str(x) for x in cup_capacity)}")
else:
    print(f"Bottles: {' '.join(str(x) for x in bottle_capacity)}")

print(f"Wasted litters of water: {wasted_water}")
