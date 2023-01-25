line = input().split('|')
result = []

for ele in range(len(line))[::-1]:
    result.extend(line[ele].split())
print(*result)
