def valid(row_pos, col_pos):
    if 0 <= row_pos < rows and 0 <= col_pos < cols:
        return True
    print("Invalid coordinates")


rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
cols = len(matrix[0])

command = input()
while command != 'END':
    action, row, col, value = [int(x) if x[-1].isdigit() else x for x in command.split()]
    if valid(row, col):
        if action == 'Add':
            matrix[row][col] += value
        elif action == 'Subtract':
            matrix[row][col] -= value

    command = input()

# [print(*matrix[row]) for row in range(rows)]

for row in range(rows):
    print(*matrix[row])