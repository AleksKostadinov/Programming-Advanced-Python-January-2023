rc = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rc)]
coordinates = [[int(y) for y in x.split(',')] for x in input().split()]

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

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y

        if 0 <= r < rc and 0 <= c < rc:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(rc) for num in matrix[row] if num > 0]
# for row in range(rc):
#     for num in matrix[row]:
#         if num > 0:
#             alive_cells.append(num)

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
# [print(*matrix[row]) for row in range(len(matrix))]
# print(*[' '.join(map(str, y)) for y in matrix], sep='\n')
[print(*[matrix[r][c] for c in range(rc)], sep=' ') for r in range(rc)]
# new_matrix = []
# for r in range(rc):
#     for c in range(rc):
#         new_matrix.append(matrix[r][c])
#     print(*new_matrix, sep=' ')
#     new_matrix = []

