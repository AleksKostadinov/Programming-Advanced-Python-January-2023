def math_operations(*args, **kwargs):
    result, pos = '', 1
    for number in args:
        if pos == 1:
            kwargs['a'] += number
        elif pos == 2:
            kwargs['s'] -= number
        elif pos == 3:
            if number != 0:
                kwargs['d'] /= number
        elif pos == 4:
            kwargs['m'] *= number
        pos += 1
        if pos > 4:
            pos = 1
    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result += f'{key}: {value:.1f}\n'
    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
