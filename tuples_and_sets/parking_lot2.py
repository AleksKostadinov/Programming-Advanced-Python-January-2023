def parking(data):
    if data:
        print('\n'.join(data))
    else:
        print('Parking Lot is Empty')


number_cars = int(input())
parking_data = set()
COMMAND_IN = 'IN'
COMMAND_OUT = 'OUT'

for record in range(number_cars):
    command, plate = input().split(', ')

    if command == COMMAND_IN:
        parking_data.add(plate)
    elif command == COMMAND_OUT:
        parking_data.remove(plate)

parking(parking_data)
