number_usernames = int(input())
unique_usernames = set()

for i in range(number_usernames):
    unique_usernames.add(input())

print('\n'.join(unique_usernames))
