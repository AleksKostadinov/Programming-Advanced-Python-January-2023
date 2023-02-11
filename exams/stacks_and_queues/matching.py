from collections import deque

males = deque(int(x) for x in input().split())
females = deque(int(x) for x in input().split())
matches = 0

while males and females:

    if females[0] <= 0:
        del females[0]
        continue
    if males[-1] <= 0:
        del males[-1]
        continue

    if females[0] % 25 == 0:
        del females[0]
        del females[0]
        continue
    if males[-1] % 25 == 0:
        del males[-1]
        del males[-1]
        continue

    first_female = females.popleft()
    last_male = males.pop()

    if first_female == last_male:
        matches += 1
    else:
        males.append(last_male - 2)

print(f"Matches: {matches}")
if not males:
    print("Males left: none")
elif males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
if not females:
    print("Females left: none")
elif females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
