import sys


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r",
               "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}


for i in range(len(CYRILLIC_SYMBOLS)):

    # Тут перевожу кирилицу в ASCII символ
    di = ord(CYRILLIC_SYMBOLS[i])

    # Тут добавляю символ с переводом в словарь TRANS
    TRANS[di] = TRANSLATION[i]


def translate():
    name = input('Впиши свое имя кирилицей: ')

    name = name.translate(TRANS)

    return name


print(translate())
