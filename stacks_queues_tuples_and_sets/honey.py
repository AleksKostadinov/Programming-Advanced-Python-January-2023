from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(map(int, input().split()))
symbol = deque(input().split())

total_honey = 0

operations = {
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar > current_bee:
        total_honey += abs(operations[symbol.popleft()](current_bee, current_nectar))
    elif current_nectar < current_bee:
        bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")

if bees:
    print(f'Bees left: {", ".join(list(map(str, bees)))}')
if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')
