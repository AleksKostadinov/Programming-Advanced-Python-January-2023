given_rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(given_rows)]

primary = []
secondary = []

for row in range(given_rows):
    primary.append(matrix[row][row])
    secondary.append(matrix[row][given_rows - row - 1])

print(abs(sum(primary) - sum(secondary)))
