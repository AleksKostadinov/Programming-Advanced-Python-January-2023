def check_valid_index(row_, col_):
    if 0 <= row_ < size and 0 <= col_ < size:
        return True


size = int(input())
matrix = [list(input()) for _ in range(size)]
removed_knights = 0

movement = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
)

while True:
    max_attacks = 0
    best_knight_pos = []
    knight_pos = []
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for move in movement:
                    pos_row = row + move[0]
                    pos_col = col + move[1]
                    if check_valid_index(pos_row, pos_col):
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    best_knight_pos = [row, col]
                    max_attacks = attacks

    if best_knight_pos:
        matrix[best_knight_pos[0]][best_knight_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
