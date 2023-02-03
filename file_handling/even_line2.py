import re

def symbols_to_be_replaced(symbol):
    return re.sub(r'[?,!.-]', '@', symbol)

with open('text.txt', 'r') as f:
    symbols = f.readlines()
    for row in range(0, len(symbols), 2):
        replaced = symbols_to_be_replaced(symbols[row]).split()
        print(' '.join(replaced[::-1]))
