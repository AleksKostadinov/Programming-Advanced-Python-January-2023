def numbers_searching(*args):
    duplicates = []
    missing_number = 0
    for number in range(min(args), max(args)):
        if args.count(number) > 1:
            duplicates.append(number)
        elif args.count(number)  == 0:
            missing_number = number
    return [missing_number, duplicates]

print(numbers_searching(1, 2, 4, 2, 5, 4))
