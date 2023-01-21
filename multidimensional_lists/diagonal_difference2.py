given_rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(given_rows)]

primary = 0
secondary = 0

for row in range(given_rows):
    primary += matrix[row][row]
    secondary += matrix[row][given_rows - row - 1]

print(abs(primary - secondary))
