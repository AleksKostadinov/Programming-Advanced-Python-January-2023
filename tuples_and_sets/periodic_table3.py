unique_elements = set()

for _ in range(int(input())):
    for el in input().split():
        unique_elements.add(el)

print('\n'.join(unique_elements))
