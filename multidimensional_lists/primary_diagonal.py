def read_matrix(rows_):
    current_matrix = []
    for row in range(rows_):
        current_matrix.append([int(x) for x in input().split()])
    return current_matrix


def get_sum_of_primary_diagonal(matrix_):
    return sum([matrix_[ele][ele] for ele in range(rows)])


rows = int(input())
matrix = read_matrix(rows)
print(get_sum_of_primary_diagonal(matrix))
