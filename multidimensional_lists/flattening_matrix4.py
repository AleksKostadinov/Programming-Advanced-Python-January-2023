rows = int(input())
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    for el in row:
        matrix.append(el)

print(matrix)
