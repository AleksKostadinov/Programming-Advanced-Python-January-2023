lines = int(input())
stack = []


def check_stack_size():
    if len(stack) != 0:
        return True


for line in range(lines):
    command = input()

    if command.startswith('1'):
        _, number = command.split()
        stack.append(int(number))
    elif check_stack_size():
        if command.startswith('2'):
            stack.pop()
        elif command.startswith('3'):
            print(f'{max(stack)}')
        elif command.startswith('4'):
            print(f'{min(stack)}')

stack.reverse()
print(', '.join(map(str, stack)))
