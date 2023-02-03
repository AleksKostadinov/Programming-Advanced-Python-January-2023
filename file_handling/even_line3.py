def symbols_to_be_replaced(symbol):
    for element in ("-", ",", ".", "!", "?"):
        symbol = symbol.replace(element, "@")
    return symbol.split('\n')[::2]


def open_file():
    with open('text.txt', 'r') as f:
        return f.read()


def show_results():
    replaced_list = symbols_to_be_replaced(open_file())
    [print(*replaced_list[row].split()[::-1]) for row in range(len(replaced_list))]


show_results()
