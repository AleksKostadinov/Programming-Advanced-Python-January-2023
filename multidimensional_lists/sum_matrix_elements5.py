rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

result = [sum(matrix[row]) for row in range(len(matrix))]

print(sum(result))
print(matrix)
