def read_matrix(rows_):
    current_matrix = []
    for row in range(rows_):
        current_matrix.append([int(x) for x in input().split()])

    return current_matrix


def get_sum_of_columns(rows_, cols_):
    matrix = read_matrix(rows_)
    sum_of_columns = []

    for col in range(cols_):
        col_sum = 0
        for row in range(rows_):
            col_sum += matrix[row][col]

        sum_of_columns.append(col_sum)

    return sum_of_columns


rows, cols = list(map(int, input().split(', ')))

[print(num) for num in get_sum_of_columns(rows, cols)]
