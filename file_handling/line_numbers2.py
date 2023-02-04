import re


def get(line_, path):
    return len(re.findall(path, line_, re.IGNORECASE))


letter = r'[a-z]'
punctuation = r"[?,!.'-]"

output_file = open('output2.txt', 'w')

with open('text2.txt', 'r') as f:
    lines = f.readlines()
    count = 1
    for line in lines:
        num_letters = get(line, letter)
        num_punctuation = get(line, punctuation)
        output_file.write(f"Line {count}: {line[:-1]} ({num_letters})({num_punctuation})\n")
        count += 1

output_file.close()
