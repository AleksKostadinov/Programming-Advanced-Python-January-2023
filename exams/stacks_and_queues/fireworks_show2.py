from collections import deque

firework_effects = deque(int(x) for x in input().split(', '))
explosive_power = deque(int(x) for x in input().split(', '))

fireworks_dict = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}
not_prepared = True

while firework_effects and explosive_power and not_prepared:

    if firework_effects[0] <= 0:
        del firework_effects[0]
        continue
    if explosive_power[-1] <= 0:
        del explosive_power[-1]
        continue

    first_firework_effect = firework_effects.popleft()
    last_explosive_power = explosive_power.pop()
    sum_value = first_firework_effect + last_explosive_power

    if sum_value % 15 == 0:
        fireworks_dict['Crossette Fireworks'] += 1
    elif sum_value % 5 == 0:
        fireworks_dict['Willow Fireworks'] += 1
    elif sum_value % 3 == 0:
        fireworks_dict['Palm Fireworks'] += 1
    else:
        firework_effects.append(first_firework_effect - 1)
        explosive_power.append(last_explosive_power)

    if all(x >= 3 for x in list(fireworks_dict.values())):
        not_prepared = False

if not_prepared:
    print("Sorry. You can't make the perfect firework show.")
else:
    print("Congrats! You made the perfect firework show!")

if firework_effects:
    print(f'Firework Effects left: {", ".join(map(str, firework_effects))}')
if explosive_power:
    print(f'Explosive Power left: {", ".join(map(str, explosive_power))}')

for key, value in fireworks_dict.items():
    print(f'{key}: {value}')