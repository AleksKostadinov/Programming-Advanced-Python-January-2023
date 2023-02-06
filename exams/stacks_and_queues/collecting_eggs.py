from collections import deque

eggs_size = deque(int(x) for x in input().split(', '))
paper_size = deque(int(x) for x in input().split(', '))

BOX_SIZE = 50

box = 0

while eggs_size and paper_size:
    first_egg = eggs_size.popleft()

    if first_egg <= 0:
        continue
    elif first_egg != 13:
        last_paper = paper_size.pop()
        if first_egg + last_paper <= BOX_SIZE:
            box += 1
    elif first_egg == 13:
        paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]

if box:
    print(f"Great! You filled {box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join(map(str, eggs_size))}")
if paper_size:
    print(f"Pieces of paper left: {', '.join(map(str, paper_size))}")

