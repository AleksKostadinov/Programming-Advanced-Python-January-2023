rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input()] for _ in range(rows)]
commands = input()

winner, movement = False, {
    "U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]
}


def find_player_position_func():
    for row in range(rows):
        if "P" in matrix[row]:
            return row, matrix[row].index("P")


def player_alive_func(row, col):
    if matrix[row][col] == "B":
        show_result_func("dead")


def check_valid_index_func(row, col, player=False):
    global winner
    if 0 <= row < rows and 0 <= col < cols:
        return True
    if player:
        winner = True


def bunnies_position_func():
    position = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                position.append(row)
                position.append(col)
    return position


def bunnies_moves_func(bunnies_pos):
    for i in range(0, len(bunnies_pos), 2):
        row, col = bunnies_pos[i], bunnies_pos[i + 1]
        for bunnie_move in movement:
            new_row, new_col = row + movement[bunnie_move][0], col + movement[bunnie_move][1]
            if check_valid_index_func(new_row, new_col):
                matrix[new_row][new_col] = "B"


def show_result_func(status="won"):
    [print(*matrix[row], sep="") for row in range(rows)]
    print(f"{status}: {player_row} {player_col}")
    exit()


player_row, player_col = find_player_position_func()
matrix[player_row][player_col] = "."
for command in commands:
    player_movement_row, player_movement_col = player_row + movement[command][0], player_col + movement[command][1]
    if check_valid_index_func(player_movement_row, player_movement_col, True):
        player_row, player_col = player_movement_row, player_movement_col
    bunnies_moves_func(bunnies_position_func())
    if winner:
        show_result_func()
    if check_valid_index_func(player_movement_row, player_movement_col):
        player_alive_func(player_movement_row, player_movement_col)

# https://github.com/ceo-py/softuni/blob/main/Python%20Advanced/Python%20Advanced%20-%20Exercises/Multidimensional%20Lists%20-%20Exercise%201/10_radioactive_mutate_vampire_bunnies.py
