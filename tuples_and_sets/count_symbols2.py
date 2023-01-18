text = input()

occurrences = set()

for letter in text:
    occurrences.add(f'{letter}: {text.count(letter)} time/s')

print(*sorted(occurrences), sep='\n')
