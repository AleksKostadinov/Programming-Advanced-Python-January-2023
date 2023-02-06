from collections import deque

mg_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))

MAX_CAFFEINE = 300
current_caffeine = 0
total_caffeine = 0

while mg_caffeine and energy_drinks:
    current_mg_caffeine = mg_caffeine.pop()
    current_energy_drinks = energy_drinks.popleft()
    current_caffeine = current_mg_caffeine * current_energy_drinks
    total_caffeine += current_caffeine

    if total_caffeine > 300:
        total_caffeine -= current_caffeine + 30
        if total_caffeine < 0:
            total_caffeine = 0
        energy_drinks.append(current_energy_drinks)

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
