def repeat_text(text_, times_):
    result = text_ * times_
    return result


text = input()

try:
    times = int(input())
    print(repeat_text(text, times))
except ValueError:
    print('Variable times must be an integer')
