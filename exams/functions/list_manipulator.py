def list_manipulator(numbers_list, command, pos, *number: int):
    if command == 'add' and pos == 'beginning':
        for num in number[::-1]:
            numbers_list.insert(0, num)
    elif command == 'add' and pos == 'end':
        for num in number:
            numbers_list.append(num)
    elif command == 'remove' and pos == 'beginning':
        if number:
            for num in number:
                numbers_list = numbers_list[num:]
        else:
            numbers_list.pop(0)
    elif command == 'remove' and pos == 'end':
        if number:
            for num in number:
                numbers_list = numbers_list[:len(numbers_list) - num]
        else:
            numbers_list.pop()
    return numbers_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 4))
print(list_manipulator([1,2,3], "remove", "beginning", 4))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
