import re


def get(line_, path):
    return len(re.findall(path, line_, re.IGNORECASE))


letter = r'[a-z]'
punctuation = r"[?,1.'-]"

with open('text2.txt', 'r') as f:
    lines = f.readlines()
    count = 1
    for line in lines:
        num_letters = get(line, letter)
        num_punctuation = get(line, punctuation)
        print(f"Line {count}: {line[:-1]} ({num_letters})({num_punctuation})")
        count += 1
