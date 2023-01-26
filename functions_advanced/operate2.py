def operate(operator, *args):
    result = args[0]
    if operator == '+':
        return sum(args)
    elif operator == '-':
        for x in args[1:]:
            result -= x
        return result
    elif operator == '*':
        for x in args[1:]:
            result *= x
        return result
    elif operator == '/':
        for x in args[1:]:
            result /= x
        return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))