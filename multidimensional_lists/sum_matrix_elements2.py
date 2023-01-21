def read_matrix_func():
    num_rows, num_columns = [int(x) for x in input().split(', ')]
    current_matrix = []

    for row in range(num_rows):
        row_data = list(map(int, input().split(', ')))
        current_matrix.append(row_data)

    return current_matrix


matrix = read_matrix_func()
matrix_ele_sum = sum([sum(current_el) for current_el in matrix])

print(matrix_ele_sum)
print(matrix)