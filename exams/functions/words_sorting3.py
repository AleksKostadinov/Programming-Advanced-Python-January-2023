def words_sorting(*args):
    result_dict, result = {}, ''

    for arg in args:
        if not arg in result_dict:
            result_dict[arg] = 0
        result_dict[arg] += sum(ord(char) for char in arg)

    if sum(result_dict.values()) % 2 == 0:
        for key in sorted(result_dict):
            result += f'{key} - {result_dict[key]}\n'
        return result
    else:
        for key, value in sorted(result_dict.items(), key=lambda x: -x[1]):
            result += f'{key} - {value}\n'
        return result

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
