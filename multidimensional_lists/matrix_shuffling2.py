def check_valid_index(index):
    if {index[0], index[2]}.issubset(valid_rows) and {index[1], index[3]}.issubset(valid_cols):
        return True
    return False


def swap_command(command, index):
    if check_valid_index(index) and command == "swap" and len(index) == 4:
        row1, col1, row2, col2 = index
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(' '.join(map(str, matrix[r]))) for r in range(rows)]
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    action, *info = [int(x) if x.isdigit() else x for x in input().split()]
    if action == "END":
        break
    swap_command(action, info)