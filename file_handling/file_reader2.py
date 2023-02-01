with open('numbers.txt', 'r') as file:
    print(sum([int(x) for x in file.read()]))
