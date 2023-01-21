given_rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(given_rows)]

primary = [matrix[row][row] for row in range(given_rows)]
secondary = [matrix[row][given_rows - row - 1] for row in range(given_rows)]

print(f'Primary diagonal: {", ".join(str(x) for x in primary)}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary)}. Sum: {sum(secondary)}')
