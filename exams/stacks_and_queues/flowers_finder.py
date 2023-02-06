from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

word_list =  {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
word_found = False
searched_word = ''

while vowels and consonants and not word_found:
    first_vowel = vowels.popleft()
    last_consonants = consonants.pop()
    for key, value in word_list.items():
        if first_vowel in value:
            word_list[key] = word_list[key].replace(first_vowel, '')
        if last_consonants in value:
            word_list[key] = word_list[key].replace(last_consonants, '')
        if len(word_list[key]) == 0:
            word_found = True
            searched_word = key
            break

if word_found:
    print(f'Word found: {searched_word}')
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(map(str, vowels))}")
if consonants:
    print(f"Consonants left: {' '.join(map(str, consonants))}")
