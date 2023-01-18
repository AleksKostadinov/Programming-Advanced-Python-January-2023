n, m = list(map(int, input().split()))

first_set = {input() for x in range(n)}
second_set = {input() for x in range(m)}

print('\n'.join(first_set.intersection(second_set)))
