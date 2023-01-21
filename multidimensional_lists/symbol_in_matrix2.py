def check_for_symbol(matrix_, symbol_):
    for row in range(len(matrix_)):
        for col in range(len(matrix_)):
            if symbol_ == matrix_[row][col]:
                return row, col


def print_func(data, symbol_):
    if data:
        print(data)
    else:
        print(f'{symbol_} does not occur in the matrix')


rows = int(input())
matrix = [list(input()) for i in range(rows)]
symbol = input()

print_func(check_for_symbol(matrix, symbol), symbol)
