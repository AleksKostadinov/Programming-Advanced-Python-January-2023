from collections import deque

energy = deque(int(x) for x in input().split())
materials = deque(int(x) for x in input().split())

made_toys = 0
total_energy_used = 0
count_boxes = 0

while energy and materials:
    first_elf = energy.popleft()
    not_enough_energy = False

    if first_elf < 5:
        continue

    last_box = materials.pop()
    count_boxes += 1

    if first_elf < last_box:
        not_enough_energy = True

    if count_boxes % 15 == 0:
        if first_elf >= last_box * 2:
            first_elf -= last_box * 2
            total_energy_used += last_box * 2
            energy.append(first_elf)
        else:
            not_enough_energy = True
    elif count_boxes % 5 == 0:
        if first_elf >= last_box:
            total_energy_used += last_box
            first_elf = (first_elf - last_box)
            energy.append(first_elf)

    elif count_boxes % 3 == 0:
        if first_elf >= last_box * 2:
            total_energy_used += last_box * 2
            first_elf = (first_elf - last_box * 2) + 1
            energy.append(first_elf)
            made_toys += 2
        else:
            not_enough_energy = True
    elif first_elf >= last_box:
        total_energy_used += last_box
        first_elf = (first_elf - last_box) + 1
        energy.append(first_elf)
        made_toys += 1

    if not_enough_energy:
        materials.append(last_box)
        first_elf *= 2
        energy.append(first_elf)

print(f"Toys: {made_toys}")
print(f"Energy: {total_energy_used}")
if energy:
    print(f'Elves left: {", ".join(map(str, energy))}')
if materials:
    print(f'Boxes left: {", ".join(map(str, materials))}')
