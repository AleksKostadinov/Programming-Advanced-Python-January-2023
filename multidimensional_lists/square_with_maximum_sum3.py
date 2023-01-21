rows, cols = (int(x) for x in input().split(", "))
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

max_sum = 0
numbers_ = []

for row in range(rows - 1):
    for col in range(cols - 1):
        first = matrix[row][col]
        second = matrix[row][col + 1]
        third = matrix[row + 1][col]
        forth = matrix[row + 1][col + 1]
        result = first + second + third + forth

        if result > max_sum:
            max_sum = result
            numbers_ = [first, second, third, forth]

print(" ".join(str(x) for x in numbers_[:2]))
print(" ".join(str(x) for x in numbers_[2:]))
print(max_sum)