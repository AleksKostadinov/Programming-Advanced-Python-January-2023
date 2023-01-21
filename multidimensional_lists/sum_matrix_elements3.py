num_rows, _ = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for row in range(num_rows)]

print(sum(list(map(sum, zip(*matrix)))))
# print(sum([sum(i) for i in zip(*matrix)]))
print(matrix)
