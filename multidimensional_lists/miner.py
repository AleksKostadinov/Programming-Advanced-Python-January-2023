from collections import deque

MATRIX_SIZE = int(input())
commands = deque(input().split())

coal = 0
collected_coal = 0
start_row, start_col = 0, 0
moving_row, moving_col = 0, 0
matrix = []
movement = {
    "up": (-1, 0), "down": (1, 0),
    "left": (0, -1), "right": (0, 1)
}

for row in range(MATRIX_SIZE):
    matrix.append(input().split())
    coal += matrix[row].count("c")
    if "s" in matrix[row]:
        start_row, start_col = row, matrix[row].index("s")

while commands:
    direction = commands.popleft()
    moving_row, moving_col = start_row + movement[direction][0], start_col + movement[direction][1]
    if not 0 <= moving_row < MATRIX_SIZE or not 0 <= moving_col < MATRIX_SIZE:
        continue

    symbol = matrix[moving_row][moving_col]

    if symbol == "e":
        print(f"Game over! {moving_row, moving_col}")
        break

    if symbol == "c":
        matrix[moving_row][moving_col] = "*"
        collected_coal += 1

    if collected_coal == coal:
        print(f"You collected all coal! {moving_row, moving_col}")
        break

    start_row, start_col = moving_row, moving_col
else:
    print(f"{coal - collected_coal} pieces of coal left. {moving_row, moving_col}")
