n, m = [int(x) for x in input().split()]
number_n = set()
number_m = set()

for i in range(n):
    number_n.add(input())
for j in range(m):
    number_m.add(input())

print(*number_n.intersection(number_m), sep='\n')
