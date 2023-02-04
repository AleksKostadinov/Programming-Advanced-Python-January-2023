from os import walk
from os.path import join

files_dict = {}
for (root, dirs, files) in walk("."):
    for file in files:
        file_name, file_extension = file.split(".")
        if file_extension not in files_dict:
            files_dict[file_extension] = []
        files_dict[file_extension].append(file)

result = []
for extension, files in sorted(files_dict.items()):
    result.append(f".{extension}\n")
    [result.append(f"- - - {file_name}\n") for file_name in sorted(files)]
with open(join(".", "report.txt"), "w") as output_file:
    output_file.writelines(result)
