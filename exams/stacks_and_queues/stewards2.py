from collections import deque

seats = input().split(', ')
first_sequence = deque(int(x) for x in input().split(', '))
second_sequence = deque(int(x) for x in input().split(', '))

rotation, matches = 0, []

while first_sequence and second_sequence:
    first = first_sequence.popleft()
    second = second_sequence.pop()
    first_symbol = str(first) + chr(first + second)
    second_symbol = str(second) + chr(first + second)
    rotation += 1

    if first_symbol in seats:
        if first_symbol not in matches:
            matches.append(first_symbol)
    elif second_symbol in seats:
        if second_symbol not in matches:
            matches.append(second_symbol)
    else:
        first_sequence.append(first)
        second_sequence.appendleft(second)

    if len(matches) == 3:
        break

    if rotation == 10:
        break

print(f'Seat matches: {", ".join(map(str, matches))}')
print(f'Rotations count: {rotation}')
