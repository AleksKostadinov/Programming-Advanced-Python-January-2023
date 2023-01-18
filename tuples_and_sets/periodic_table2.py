number_lines = int(input())

unique_elements = set()

for _ in range(number_lines):
    elements = input().split()
    for el in elements:
        unique_elements.add(el)
print(*unique_elements, sep='\n')
