SIZE = 6

matrix = [input().split() for _ in range(SIZE)]
row, col = [int(x) for x in input()[1:-1].split(",")]
# row, col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()

while command != 'Stop':
    action, direction, *other = command.split(', ')
    row = row + directions[direction][0]
    col = col + directions[direction][1]
    if action == "Create":
        if matrix[row][col] == ".":
            matrix[row][col] = other[0]
    elif action == "Update":
        if matrix[row][col] != ".":
            matrix[row][col] = other[0]
    elif action == "Delete":
        if matrix[row][col] != ".":
            matrix[row][col] = "."
    elif action == "Read":
        if matrix[row][col] != ".":
            print(matrix[row][col])

    command = input()

[print(*matrix[row]) for row in range(SIZE)]
