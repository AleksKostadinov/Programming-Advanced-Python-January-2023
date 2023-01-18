occurrences = {}

for letter in input():
    if letter not in occurrences:
        occurrences[letter] = 0
    occurrences[letter] += 1

for k, v in sorted(occurrences.items()):
    print(f'{k}: {v} time/s')
