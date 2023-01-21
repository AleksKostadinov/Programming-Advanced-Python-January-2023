rows, cols = [int(x) for x in input().split()]

for row in range(97, 97 + rows):
    for col in range(97, 97 + cols):
        words = chr(row) + chr(col + row - 97) + chr(row)
        print(words, end=' ')
    print()
