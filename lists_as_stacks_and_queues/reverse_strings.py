text = list(input())
stack = []

for i in range(len(text)):
    text_popped = text.pop()
    stack.append(text_popped)
print(''.join(stack))
