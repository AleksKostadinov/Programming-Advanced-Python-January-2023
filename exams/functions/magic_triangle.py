def get_magic_triangle(n):
    result = []
    for row in range(n):
        result.append([])
        result[row].append(1)
        for col in range(1, row):
            result[row].append(result[row - 1][col - 1] + result[row - 1][col])
        if row != 0:
            result[row].append(1)
    return result

print(get_magic_triangle(5))
