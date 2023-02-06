from collections import deque

seats = input().split(', ')
first_sequence = deque(int(x) for x in input().split(', '))
second_sequence = deque(int(x) for x in input().split(', '))

seat_matches = []
rotation = 0

while len(seat_matches) != 3 and rotation != 10:
    first = first_sequence.popleft()
    second = second_sequence.pop()
    sum_first_second = first + second
    ascii_char = chr(sum_first_second)
    first_try = str(first) + ascii_char
    second_try = str(second) + ascii_char

    for seat in [first_try, second_try]:
        if seat in seats:
            if seat not in seat_matches:
                seat_matches.append(seat)
                break
    else:
        first_sequence.append(first)
        second_sequence.appendleft(second)

    rotation += 1

print(f'Seat matches: {", ".join(seat_matches)}')
print(f'Rotations count: {rotation}')
