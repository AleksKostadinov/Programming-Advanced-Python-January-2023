def start_spring(**kwargs):
    result_dict = {}
    result = ''
    for objects, types in kwargs.items():
        if not types in result_dict:
            result_dict[types] = []
        result_dict[types].append(objects)
    for keys, values in sorted(result_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f'{keys}:\n'
        for value in sorted(values):
            result += f'-{value}\n'
    return result

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))




