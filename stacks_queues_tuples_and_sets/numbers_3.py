first_set = set(int(x) for x in input().split())
second_set = set(map(int, input().split()))

for _ in range(int(input())):
    action, *data = input().split()

    if action == "Add":
        if data[0] == "First":
            first_set = first_set.union([int(x) for x in data[1:]])
        else:
            second_set = second_set.union([int(x) for x in data[1:]])
    elif action == "Remove":
        if data[0] == "First":
            first_set = first_set.difference([int(x) for x in data[1:]])
        else:
            second_set = second_set.difference([int(x) for x in data[1:]])
    else:
        print(first_set.issuperset(second_set))

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
