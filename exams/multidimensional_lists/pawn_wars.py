def winner_func(pawn_, row_):
    if pawn_ == 'white' and row_ == 0:
        return True
    elif pawn_ == 'black' and row_ == SIZE - 1:
        return True
    return False


def move_func(pawn_, move_row, move_col):
    return [move_row - 1, move_col] if pawn_ == 'white' else [move_row + 1, move_col]


def capture_func(pawn_, white_row_, white_col_, black_row_, black_col_):
    if pawn_ == 'white':
        if (white_col_ - 1, white_row_ - 1) == (black_col_, black_row_):
            return black_row_, black_col_
        elif (white_col_ + 1, white_row_ - 1) == (black_col_, black_row_):
            return black_row_, black_col_
    elif pawn_ == 'black':
        if (black_col_ + 1, black_row_ + 1) == (white_col_, white_row_):
            return white_row_, white_col_
        elif (black_col_ - 1, black_row_ + 1) == (white_col_, white_row_):
            return white_row_, white_col_
    return None


SIZE = 8
matrix = []
pawns = ['white', 'black']
white_row, white_col, black_row, black_col = 0, 0, 0, 0
capture = False
capture_col, capture_row = 0, 0

for row in range(SIZE):
    matrix.append(input().split())
    if "w" in matrix[row]:
        white_row, white_col = row, matrix[row].index("w")
    if "b" in matrix[row]:
        black_row, black_col = row, matrix[row].index("b")

while True:
    pawn = pawns[0]

    if capture_func(pawn, white_row, white_col, black_row, black_col):
        capture_row, capture_col = capture_func(pawn, white_row, white_col, black_row, black_col)
        winner = pawn.capitalize()
        capture = True
        break

    if pawn == 'white':
        white_row, white_col = move_func(pawn, white_row, white_col)
        if winner_func(pawn, white_row):
            winner = pawn.capitalize()
            break
    elif pawn == 'black':
        black_row, black_col = move_func(pawn, black_row, black_col)
        if winner_func(pawn, black_row):
            winner = pawn.capitalize()
            break

    pawns[0], pawns[1] = pawns[1], pawns[0]

winner_col = white_col if pawn == 'white' else black_col
winner_row = SIZE - white_row if pawn == 'white' else SIZE - black_col
ascii_col = chr(97 + winner_col)
ascii_capture_coll = chr(97 + capture_col)

if capture:
    print(f"Game over! {winner} win, capture on {ascii_capture_coll}{SIZE - capture_row}.")
else:
    print(f"Game over! {winner} pawn is promoted to a queen at {ascii_col}{winner_row}.")
