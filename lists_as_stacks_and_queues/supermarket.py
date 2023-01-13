name = input()
queue = []
count = 0

while name != 'End':
    if name == 'Paid':
        print('\n'.join(queue))
        queue = []
        count = 0
    else:
        queue.append(name)
        count += 1
    name = input()
print(f'{count} people remaining.')
