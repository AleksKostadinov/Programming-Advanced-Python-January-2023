from collections import deque


def check_under_100(result_, last_material_, first_magic_):
    if result_ % 2 == 0:
        last_material_ *= 2
        first_magic_ *= 3
        result_ = last_material_ + first_magic_
        return result_
    result_ = 2 * (last_material_ + first_magic_)
    return result_


def check_100_to_499():
    if 100 <= result <= 199:
        presents['Gemstone'] += 1
    elif 200 <= result <= 299:
        presents['Porcelain Sculpture'] += 1
    elif 300 <= result <= 399:
        presents['Gold'] += 1
    elif 400 <= result <= 499:
        presents['Diamond Jewellery'] += 1
    return presents


materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

presents = {
            "Diamond Jewellery": 0,
            "Gemstone": 0,
            "Gold": 0,
            "Porcelain Sculpture": 0
            }

while materials and magic_level:

    last_material = materials.pop()
    first_magic = magic_level.popleft()
    result = last_material + first_magic

    if result < 100:
        result = check_under_100(result, last_material, first_magic)

    if result > 499:
        result = (last_material + first_magic) / 2

    if 100 <= result <= 499:
        present = check_100_to_499()

if (presents["Gemstone"] > 0 and presents["Porcelain Sculpture"] > 0) \
        or (presents["Gold"] > 0 and presents["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for key, value in sorted(presents.items()):
    if value > 0:
        print(f"{key}: {value}")
