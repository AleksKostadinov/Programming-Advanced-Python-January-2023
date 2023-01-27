from collections import deque


def math_operations(*args, **kwargs):
    args = deque(args)
    while args:
        for key, value in kwargs.items():
            if args:
                if key == "d" and args[0] == 0:
                    args.popleft()
                    continue
                kwargs[key] = operators[key](value, args.popleft())

    result = {key: value for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))}
    return "\n".join(f"{key}: {value:.1f}" for key, value in result.items())


operators = {
    "a": lambda x, y: x + y,
    "s": lambda x, y: x - y,
    "d": lambda x, y: x / y,
    "m": lambda x, y: x * y,
}

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
