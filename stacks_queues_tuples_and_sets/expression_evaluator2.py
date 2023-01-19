from collections import deque

expression = input().split()
numbers_queue = deque()

operators = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}

for element in expression:
    if element in operators:
        while len(numbers_queue) > 1:
            numbers_queue.appendleft(operators[element](numbers_queue.popleft(), numbers_queue.popleft()))
    else:
        numbers_queue.append(int(element))
print(*numbers_queue)
