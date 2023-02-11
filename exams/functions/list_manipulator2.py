def list_manipulator(numbers_list, command, pos, *number: int):
    if command == 'add':
        return list(number) + numbers_list if pos == "beginning" else numbers_list + list(number)
    elif command == 'remove':
        if pos == "beginning":
            return numbers_list[number[0]:] if number else numbers_list[1:]
        elif pos == "end":
            return numbers_list[:len(numbers_list) - number[0]] if number else numbers_list[:-1]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 3))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
