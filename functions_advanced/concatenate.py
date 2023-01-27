def concatenate(*args, **kwargs):
    result = ''.join(args)
    for key in kwargs:
        result = result.replace(key, kwargs[key])
    return result


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
