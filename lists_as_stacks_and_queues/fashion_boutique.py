clothes = [int(x) for x in input().split()]
rack = int(input())

rack_counter = 1
current_rack = rack

while clothes:
    cloth = clothes.pop()
    if current_rack >= cloth:
        current_rack -= cloth
    else:
        rack_counter += 1
        current_rack = rack
        current_rack -= cloth
print(rack_counter)
