rows, cols = (int(x) for x in input().split(", "))
result = 0
matrix = []

for _ in range(rows):
    row_data = [int(x) for x in input().split(', ')]
    matrix.append(row_data)
    result += sum(row_data)

print(result)
print(matrix)
