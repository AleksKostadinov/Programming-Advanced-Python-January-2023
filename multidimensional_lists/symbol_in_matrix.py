def read_matrix(rows_):
    current_matrix = []
    for row in range(rows_):
        current_matrix.append(list(input()))
    return current_matrix


def check_for_symbol(matrix_, symbol_):
    for row in range(len(matrix_)):
        for col in range(len(matrix_[row])):
            current_element = matrix_[row][col]
            if current_element == symbol_:
                return row, col


def print_func(data, symbol_):
    if data:
        print(data)
    else:
        print(f'{symbol_} does not occur in the matrix')


rows = int(input())
matrix = read_matrix(rows)
symbol = input()


print_func(check_for_symbol(matrix, symbol), symbol)
