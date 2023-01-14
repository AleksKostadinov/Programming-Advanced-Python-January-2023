lines = int(input())
stack = []

for line in range(lines):
    number = [int(x) for x in input().split()]

    if number[0] == 1:
        stack.append(number[1])
    elif number[0] == 2:
        stack.pop() if stack else None,
    elif number[0] == 3:
        print(f'{max(stack)}') if stack else None,
    elif number[0] == 4:
        print(f'{min(stack)}') if stack else None,

stack.reverse()

print(', '.join(map(str, stack)))