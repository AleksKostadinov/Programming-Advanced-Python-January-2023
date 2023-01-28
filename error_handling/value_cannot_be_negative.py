class ValueCannotBeNegative(Exception):
    """If a negative number occurs, raise the exception"""
    pass


for _ in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative
