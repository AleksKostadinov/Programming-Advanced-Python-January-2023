file = open('numbers.txt')
total_sum = 0

for num in file:
    total_sum += int(num)
print(total_sum)