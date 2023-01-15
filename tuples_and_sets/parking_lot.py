number_cars = int(input())
parking_lot = [input() for _ in range(number_cars)]

parking_data = set()
COMMAND_IN = 'IN'
COMMAND_OUT = 'OUT'

for record in parking_lot:
    command, plate = record.split(', ')

    if command == COMMAND_IN:
        parking_data.add(plate)
    elif command == COMMAND_OUT:
        parking_data.remove(plate)

if parking_data:
    print('\n'.join(parking_data))
else:
    print('Parking Lot is Empty')
