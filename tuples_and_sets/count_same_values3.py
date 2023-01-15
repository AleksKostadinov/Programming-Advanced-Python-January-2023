values = tuple(map(float, input().split()))
result = {float(key): values.count(key) for key in values}

[print(f"{k:.1f} - {v} times") for k, v in result.items()]
