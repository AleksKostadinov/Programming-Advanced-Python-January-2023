from collections import deque

parentheses = deque(input())
open_par = deque()
balanced = True

parenthesis_dict = {
    "{": "}",
    "[": "]",
    "(": ")"
}

for element in parentheses:
    if element in "{[(":
        open_par.append(element)
    else:
        if open_par:
            check = open_par.pop()
            if parenthesis_dict[check] != element:
                balanced = False
                break
        else:
            balanced = False
            break
if balanced:
    print("YES")
else:
    print("NO")