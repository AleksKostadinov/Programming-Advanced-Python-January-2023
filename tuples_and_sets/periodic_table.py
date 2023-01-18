from collections import deque
number_lines = int(input())

elements = [input() for _ in range(number_lines)]
unique_elements = set()

for el in elements:
    el = deque(el.split())
    while el:
        unique_elements.add(el[0])
        el.popleft()
print(*unique_elements, sep='\n')
