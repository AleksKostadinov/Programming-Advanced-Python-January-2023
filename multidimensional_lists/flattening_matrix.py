rows = int(input())
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

new_matrix = []

for current_matrix in matrix:
    for element in current_matrix:
        new_matrix.append(element)

print(new_matrix)
