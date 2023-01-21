def is_even(number):
    return number % 2 == 0


def matrix_even_numbers(matrix):
    matrix_even_only = [[i for i in row if is_even(i)] for row in matrix]
    return matrix_even_only


rows_number = int(input())
matrix = [[int(i) for i in input().split(", ")] for _ in range(rows_number)]
result_matrix = matrix_even_numbers(matrix)
print(result_matrix)
