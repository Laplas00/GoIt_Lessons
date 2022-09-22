from multiprocessing import Value
from optparse import Values
from platform import architecture

articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

# Тут используем перебор по спискам в одном цикле
# А вложенный цикл уже перебираает елементы dict
# --------------------------------------------------
# Для удобства использую i.values, который в отличии
# от .keys()  (который тоже в цикле используется)
# перебирает именно значения.


def find_articles(key, letter_case=False):
    result = []
    for i in articles_dict:
        for elem in i.values():
            if letter_case == False:
                key = key.lower()
                if type(elem) != int:

                    elem = elem.lower()
                    finder = elem.find(key)
                    if finder != -1:
                        result.append(i)

                else:
                    break
            else:
                if type(elem) != int:
                    finder = elem.find(key)
                    if finder != -1:
                        result.append(i)
    print(result)


print(find_articles("Ocean", True))
