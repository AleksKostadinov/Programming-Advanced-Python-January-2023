from string import punctuation

with open('text2.txt', 'r') as f:
   text = f.readlines()

output_file = open('output2.txt', 'w')

for i in range(len(text)):
    row = text[i]

    letter = 0
    punct = 0

    for symbol in row:
        if symbol.isalpha():
            letter += 1
        elif symbol in punctuation:
            punct += 1

    output_file.write(f'Line {i+1}: {"".join(row[:-1])} ({letter})({punct})\n')

output_file.close()
