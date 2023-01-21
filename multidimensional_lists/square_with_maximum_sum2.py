def submatrix(rows_num_, cols_num_, matrix_):
    max_sum = 0
    matrix_coordinates = []
    for row in range(rows_num_ - 1):
        for col in range(cols_num_ - 1):
            current_sum = matrix_[row][col] + matrix_[row + 1][col] + matrix_[row][col + 1] \
                          + matrix_[row + 1][col + 1]
            if current_sum > max_sum:
                max_sum = current_sum
                matrix_coordinates = [row, col]
    sub_row, sub_col = matrix_coordinates
    found_matrix = [
        [matrix[sub_row][sub_col], matrix[sub_row][sub_col + 1]],
        [matrix[sub_row + 1][sub_col], matrix[sub_row + 1][sub_col + 1]]
    ]
    return found_matrix, max_sum


rows_num, cols_num = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows_num)]

submatrix_coordinates, sum_of_elements = submatrix(rows_num, cols_num, matrix)

for coordinate in submatrix_coordinates:
    print(*coordinate)
print(sum_of_elements)