text = input()
stack = []

for i, d in enumerate(text):
    if d == '(':
        stack.append(i)
    elif d == ')':
        last = stack.pop()
        print(text[last: i + 1])
