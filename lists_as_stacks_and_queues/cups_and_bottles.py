from collections import deque

cup_capacity = deque([int(x) for x in input().split()])
bottle_capacity = list(map(int, input().split()))

wasted_water = 0

while cup_capacity and bottle_capacity:
    bottle = bottle_capacity.pop()
    cup_capacity[0] -= bottle

    if cup_capacity[0] <= 0:
        wasted_water += abs(cup_capacity[0])
        del cup_capacity[0]

if cup_capacity:
    print(f"Cups: {' '.join(str(x) for x in cup_capacity)}")
else:
    print(f"Bottles: {' '.join(str(x) for x in bottle_capacity)}")
print(f"Wasted litters of water: {wasted_water}")
