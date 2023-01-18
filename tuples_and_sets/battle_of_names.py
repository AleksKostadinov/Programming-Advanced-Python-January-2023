odd_set = set()
even_set = set()
rows = int(input())

for row in range(1, rows + 1):
    ascii_name = sum(ord(letter) for letter in input()) // row

    if ascii_name % 2 == 0:
        even_set.add(ascii_name)
    else:
        odd_set.add(ascii_name)

if sum(odd_set) > sum(even_set):
    print(*(odd_set.difference(even_set)), sep=', ')
elif sum(odd_set) < sum(even_set):
    print(*(odd_set.symmetric_difference(even_set)), sep=', ')
else:
    print(*(odd_set.union(even_set)), sep=', ')
