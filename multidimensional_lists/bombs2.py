matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

directions = (
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
    (0, -1),  # left
    (-1, 1),  # top-right
    (-1, -1),  # top-left
    (1, -1),  # bottom-left
    (1, 1),  # bottom-right
    (0, 0),  # current (this should be last)
)

for row, col in [[int(n) for n in x.split(",")] for x in input().split(" ")]:
    if matrix[row][col] <= 0:
        continue

    bomb_damage = matrix[row][col]
    for x, y in directions:
        if 0 <= row + x < len(matrix) and 0 <= col + y < len(matrix):
            matrix[row + x][col + y] -= bomb_damage if matrix[row + x][col + y] > 0 else 0

alive_cells = [num for row in range(len(matrix)) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}\nSum: {sum(alive_cells)}")
[print(*matrix[row]) for row in range(len(matrix))]
