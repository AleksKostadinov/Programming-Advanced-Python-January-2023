number = int(input())
names = set()

for _ in range(number):
    names.add(input())

print('\n'.join(names))
