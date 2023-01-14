from collections import deque

parentheses = deque(input())
open_par = deque()
balanced = True

while parentheses:
    check = parentheses.popleft()
    if check in "{[(":
        open_par.append(check)
    elif not open_par:
        balanced = False
        break
    else:
        if f'{open_par.pop() + check}' not in "{}()[]":
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")
