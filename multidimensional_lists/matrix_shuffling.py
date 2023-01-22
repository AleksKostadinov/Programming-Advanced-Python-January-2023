def check_valid(row1_, col1_, row2_, col2_):
    if 0 <= row1_ < rows and 0 <= col1_ < cols and 0 <= row2_ < rows and 0 <= col2_ < cols:
        return True
    print('Invalid input!')


def swap_func(row1_, col1_, row2_, col2_):
    if check_valid(row1_, col1_, row2_, col2_):
        matrix[row1_][col1_], matrix[row2_][col2_] = matrix[row2_][col2_], matrix[row1_][col1_]
        for row in range(len(matrix)):
            print(' '.join(map(str, matrix[row])))


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

command = input()

while command != 'END':
    action, *info = [int(x) if x.isdigit() else x for x in command.split()]
    if action == 'swap' and len(info) == 4:
        row1, col1, row2, col2 = info
        swap_func(row1, col1, row2, col2)
    else:
        print('Invalid input!')
    command = input()
