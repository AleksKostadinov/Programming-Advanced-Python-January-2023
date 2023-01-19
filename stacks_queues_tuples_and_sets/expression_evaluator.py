from functools import reduce

expression = input().split()

idx = 0

functions = {
    "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
    "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
    "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
    "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
}

while idx < len(expression):
    element = expression[idx]

    if element in "*/+-":
        expression[0] = functions[element](idx)
        [expression.pop(1) for i in range(idx)]
        idx = 0

    idx += 1

print(int(expression[0]))
