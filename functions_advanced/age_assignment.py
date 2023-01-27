def age_assignment(*args, **kwargs):
    result = []
    for name in args:
        for key, value in kwargs.items():
            if name.startswith(key):
                result.append(f'{name} is {value} years old.')
    return '\n'.join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))