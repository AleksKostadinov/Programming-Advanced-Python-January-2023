import os

result = {}

for _, _, files in os.walk('.'):
    for file in files:
        extension = file.split('.')[-1]
        if extension not in result:
            result[extension] = []
        result[extension].append(file)

sorted_result = sorted(result)

with open('./report.txt', 'w') as file:
    for key in sorted_result:
        file.write(f'.{key}\n')
        for element in sorted(result[key]):
            file.write(f'- - - {element}\n')
