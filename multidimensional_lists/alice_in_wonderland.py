def check_valid(row, col):
    if 0 <= row < size and 0 <= col < size and matrix[row][col] != 'X':
        return True


def find_alice(sizes):
    for row in range(sizes):
        for col in range(sizes):
            if matrix[row][col] == 'A':
                return row, col


size = int(input())
matrix = [[x for x in input().split()] for _ in range(size)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
collected_tea = 0

alice_row, alice_col = find_alice(size)

while collected_tea < 10:
    matrix[alice_row][alice_col] = '*'
    command = input()

    alice_row += directions[command][0]
    alice_col += directions[command][1]

    if not check_valid(alice_row, alice_col):
        break

    elif matrix[alice_row][alice_col] == 'R':
        matrix[alice_row][alice_col] = '*'
        break

    elif matrix[alice_row][alice_col] == "." or matrix[alice_row][alice_col] == "*":
        matrix[alice_row][alice_col] = "*"
        continue
    else:
        collected_tea += int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col] = '*'

if collected_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*matrix[row]) for row in range(size)]
