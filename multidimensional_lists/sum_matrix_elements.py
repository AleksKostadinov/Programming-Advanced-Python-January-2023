def read_matrix_func():
    num_rows, num_columns = [int(x) for x in input().split(', ')]
    current_matrix = []

    for row in range(num_rows):
        row_data = list(map(int, input().split(', ')))
        current_matrix.append(row_data)

    return current_matrix


matrix = read_matrix_func()
matrix_ele_sum = 0

for i in range(len(matrix)):
    current_row = matrix[i]
    matrix_ele_sum += sum(current_row)

print(matrix_ele_sum)
print(matrix)
