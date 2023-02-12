from collections import deque


def best_list_pureness(number_list, rotates):
    number_list = deque(number_list)
    max_result = -1000
    max_rotation = 0
    for rotate in range(rotates + 1):
        current_sum = 0
        for number in number_list:
            # for index, number in enumerate(number_list):
            #     current_sum += number * index
            current_sum += number * number_list.index(number)
        if current_sum > max_result:
            max_result = current_sum
            max_rotation = rotate
        number_list.appendleft(number_list.pop())
        # number_list.rotate()
    return f'Best pureness {max_result} after {max_rotation} rotations'


test = ([4, 3, 2, 6], 4)
# test = ([7, 9, 2, 5, 3, 4], 3)
# test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
