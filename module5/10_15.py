
from itertools import tee
import re


def find_word(text, word):
    find = re.search(word, text)
    boolean = False if find == None else True
    if boolean is True:
        nums = [x for x in find.span()]
    else:
        nums = [None, None]

    result = {
        'result': boolean,
        'first_index': nums[0],
        'last_index': nums[1],
        'search_string': word,
        'string': text
    }
    return result


all = 'Guido van Rossum began working on Python inthe late 1980s, as a successor to the ABC programming language,and first released it in 1991 as Python 0.9.0,Python'


print(find_word(all, 'python'))

# Напишите функцию find_word, которая принимает два
# параметра: первый text и второй word.
#  Функция выполняет поиск указанного слова word
#   в тексте text с помощью функции
#    search и возвращает словарь.
