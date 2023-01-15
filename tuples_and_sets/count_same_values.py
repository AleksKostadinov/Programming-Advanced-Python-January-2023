values = tuple(map(float, input().split()))
numbers_occurrence = {}

for number in values:
    if number not in numbers_occurrence:
        numbers_occurrence[number] = 0
    numbers_occurrence[number] += 1

for key, value in numbers_occurrence.items():
    print(f'{key:.1f} - {value} times')
