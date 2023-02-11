from collections import deque

effects = deque(int(x) for x in input().split(', '))
casings = deque(int(x) for x in input().split(', '))

successful = False
bombs = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120,
}
created = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0,
}
while effects and casings and not successful:
    first_effect = effects.popleft()
    last_casings = casings.pop()
    sum_values = first_effect + last_casings

    for bomb, value in bombs.items():
        if sum_values == value:
            created[bomb] += 1
            break
    else:
        effects.appendleft(first_effect)
        casings.append(last_casings - 5)

    successful = all(x>=3 for x in created.values())

if successful:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f'Bomb Effects: {", ".join(map(str, effects))}')
else:
    print("Bomb Effects: empty")

if casings:
    print(f'Bomb Casings: {", ".join(map(str, casings))}')
else:
    print("Bomb Casings: empty")

for bomb, count in created.items():
    print(f'{bomb}: {count}')
