def data_arrived_guests():
    arrived_list = []
    while True:
        data = input()
        if data == 'END':
            break
        arrived_list.append(data)
    return arrived_list


def print_func(not_arrived_guests_):
    print(len(not_arrived_guests_))
    for not_arrived in sorted(not_arrived_guests_):
        print(not_arrived)


number_guest = int(input())
reservations_list = [input() for _ in range(number_guest)]

arrived_guests = data_arrived_guests()
not_arrived_guests = set(reservations_list).difference(arrived_guests)
print_func(not_arrived_guests)
