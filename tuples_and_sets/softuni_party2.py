number_guests = int(input())

reservation = {input() for _ in range(number_guests)}
arrived_guests = input()

while arrived_guests != "END":
    reservation.remove(arrived_guests)
    arrived_guests = input()

print(len(reservation))
print("\n".join(sorted(reservation)))
