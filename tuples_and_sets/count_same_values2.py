values = tuple([float(x) for x in input().split()])
numbers_occurrence = {}

for number in values:
    if number not in numbers_occurrence:
        numbers_occurrence[number] = 0
    numbers_occurrence[number] += 1

[print(f'{k:.1f} - {v} times') for k, v in numbers_occurrence.items()]
