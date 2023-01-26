def rectangle(a, b):
    def area():
        return a * b

    def perimeter():
        return 2 * (a + b)

    if type(a) != int or type(b) != int:
        return f"Enter valid values!"

    return f'Rectangle area: {area()}\nRectangle perimeter: {perimeter()}'


print(rectangle(2, 10))
