def operate(operator, *args):
    def add():
        return sum(args)

    def subtract():
        result = args[0]
        for element in args[1::]:
            result -= element
        return result

    def multiply():
        result = 1
        for x in args:
            result *= x
        return result

    def divide():
        result = args[0]
        for x in args[1:]:
            if x == 0:
                continue
            else:
                result /= x
        return result

    if operator == "+":
        return add()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("-", 3, 2))
print(operate("/", 6, 2))