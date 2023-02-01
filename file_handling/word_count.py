import re


def read_searched_words():
    with open('words.txt') as file:
        searched_word = file.read().split()
        searched_word = [word.lower() for word in searched_word]
    return searched_word


def calculate_words(searched_word):
    with open('input.txt') as file:
        words_count = {}
        text = file.read().lower()
        for word in searched_word:
            pattern = fr'\b{word}\b'
            count = len(re.findall(pattern, text))
            words_count[word] = count
    return words_count


def result_store(results):
    with open('output.txt', 'w') as file:
        sorted_result = sorted(results.items(), key=lambda x: -x[1])
        for key, value in sorted_result:
            file.writelines(f"{key} - {value}\n")

words = read_searched_words()
result = calculate_words(words)
result_store(result)