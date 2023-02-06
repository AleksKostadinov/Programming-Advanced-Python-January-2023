def words_sorting(*args):
    words_dict = {}
    total_sum = 0
    result = ''
    for arg in args:
        words_dict[arg] = sum(ord(char) for char in arg)
        total_sum += words_dict[arg]
    if total_sum % 2 == 0:
        for key, value in sorted(words_dict.items(), key=lambda x: x[0]):
            result += f'{key} - {value}\n'
    else:
        for key, value in sorted(words_dict.items(), key=lambda x: -x[1]):
            result += f'{key} - {value}\n'
    return result

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

