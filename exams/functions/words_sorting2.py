def words_sorting(*args):
    result = ''
    words_dict = {char: sum(map(ord, char)) for char in args}

    if sum(words_dict.values()) % 2 == 0:
        for key, value in sorted(words_dict.items(), key=lambda x: x[0]):
            result += f'{key} - {value}\n'
    else:
        for key, value in sorted(words_dict.items(), key=lambda x: -x[1]):
            result += f'{key} - {value}\n'
    return result

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
