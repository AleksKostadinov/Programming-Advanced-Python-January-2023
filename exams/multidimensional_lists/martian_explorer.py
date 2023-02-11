matrix = []
water, concrete, metal, rover_row, rover_col = 0, 0, 0, 0, 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
SIZE = 6
for row in range(SIZE):
    matrix.append(input().split())
    if "E" in matrix[row]:
        rover_row = row
        rover_col = matrix[row].index("E")

commands = input().split(', ')

for command in commands:
    rover_row += directions[command][0]
    rover_col += directions[command][1]

    if rover_row < 0:
        rover_row = SIZE - 1
    elif rover_row == SIZE:
        rover_row = 0
    elif rover_col < 0:
        rover_col = SIZE - 1
    elif rover_col == SIZE:
        rover_col = 0

    step_on = matrix[rover_row][rover_col]

    if step_on == "W":
        water += 1
        print(f"Water deposit found at ({rover_row}, {rover_col})")
    elif step_on == "M":
        metal += 1
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
    elif step_on == "C":
        concrete += 1
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
    elif step_on == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if water and concrete and metal:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")