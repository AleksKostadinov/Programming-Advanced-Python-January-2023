def check_valid_index(row, col):
    return 0 <= row < SIZE and 0 <= col < SIZE


def score(col_, total_score_):
    for row_ in range(SIZE):
        total_score_ += matrix[row_][col_]
    return total_score_


SIZE = 6
THROWS = 3
prize, total_score = '', 0

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(SIZE)]

for throw in range(THROWS):
    row, col = [int(x) for x in input()[1:-1].split(', ')]

    if check_valid_index(row, col) and matrix[row][col] == 'B':
        matrix[row][col] = 0
        total_score = score(col, total_score)

if total_score < 100:
    total_score -= 100
    print(f"Sorry! You need {abs(total_score)} points more to win a prize.")
else:
    if total_score <= 199:
        prize = "Football"
    elif total_score <= 299:
        prize = "Teddy Bear"
    elif total_score >= 300:
        prize = "Lego Construction Set"
    print(f"Good job! You scored {total_score} points, and you've won {prize}.")
