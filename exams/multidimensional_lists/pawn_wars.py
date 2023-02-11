def winner_func(pawn_, row_):
    if pawn_ == 'white' and row_ == 0:
        return True
    elif pawn_ == 'black' and row_ == SIZE - 1:
        return True
    return False


def move_func(pawn_, move_row, move_col):
    return [move_row - 1, move_col] if pawn_ == 'white' else [move_row + 1, move_col]


def promoted_queen(pawn_, white_row_, white_col_, black_row_, black_col_):
    if pawn_ == 'white':
        if (white_row_ - 1, white_col_ - 1) == (black_row_, black_col_):
            return True
        elif (white_row_ - 1, white_col_ + 1) == (black_row_, black_col_):
            return True
    elif pawn_ == 'black':
        if (black_row_ + 1, black_col_ - 1) == (white_row_, white_col_):
            return True
        elif (black_row_ + 1, black_col_ + 1) == (white_row_, white_col_):
            return True
    return False


SIZE = 8
matrix = []
pawns = ['white', 'black']
white_row, white_col, black_row, black_col = 0, 0, 0, 0
capture = False

for row in range(SIZE):
    matrix.append(input().split())
    if "w" in matrix[row]:
        white_row, white_col = row, matrix[row].index("w")
    if "b" in matrix[row]:
        black_row, black_col = row, matrix[row].index("b")

while True:
    pawn = pawns[0]

    if promoted_queen(pawn, white_row, white_col, black_row, black_col):
        winner = pawn
        capture = True
        if winner == 'white':
            white_row, white_col = black_row, black_col
        else:
            black_row, black_col = white_row, white_col
        break

    if pawn == 'white':
        white_row, white_col = move_func(pawn, white_row, white_col)
        if winner_func(pawn, white_row):
            winner = pawn
            break
    elif pawn == 'black':
        black_row, black_col = move_func(pawn, black_row, black_col)
        if winner_func(pawn, black_row):
            winner = pawn
            break

    pawns[0], pawns[1] = pawns[1], pawns[0]

winner_col = white_col if pawn == 'white' else black_col
winner_row = white_row if pawn == 'white' else black_row
ascii_col = chr(97 + winner_col)


if capture:
    print(f"Game over! {winner.capitalize()} win, capture on {ascii_col}{SIZE - winner_row}.")
else:
    print(f"Game over! {winner.capitalize()} pawn is promoted to a queen at {ascii_col}{SIZE - winner_row}.")
