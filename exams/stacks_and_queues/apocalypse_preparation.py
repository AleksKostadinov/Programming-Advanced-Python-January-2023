from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

resources_needed = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100,
}
created_items = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0,
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    value_items = textile + medicament

    if value_items in [30, 40, 100]:
        if value_items == 30:
            created_items['Patch'] += 1
        elif value_items == 40:
            created_items['Bandage'] += 1
        elif value_items == 100:
            created_items['MedKit'] += 1

    elif value_items > resources_needed['MedKit']:
            created_items['MedKit'] += 1
            medicaments[-1] += value_items - 100

    else:
        medicament += 10
        medicaments.append(medicament)

if not textiles and not medicaments:
    print('Textiles and medicaments are both empty.')
elif not textiles:
    print('Textiles are empty.')
elif not medicaments:
    print('Medicaments are empty.')


for key, value in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
        if value:
            print(f"{key} - {value}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")

if medicaments:
    print(f"Medicaments left: {', '.join(map(str, reversed(medicaments)))}")
