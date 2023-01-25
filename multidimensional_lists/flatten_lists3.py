matrix = input().split('|')[::-1]

for sublist in matrix:
    for num in sublist.split():
        print(num, end=' ')