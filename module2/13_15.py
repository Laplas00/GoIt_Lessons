
from curses.ascii import isupper


message = input("Введите сообщение:")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
# цикл в котором перебираем и смещаем буквы
for ch in message:
    if not ch.isalpha():
        encoded_message += ch
        continue
    pos = ord(ch.lower()) - ord('a')
    pos = (pos - offset) % 26
    new_char = chr(pos+ord('a'))
    if ch.isupper():
        new_char = new_char.upper()
    encoded_message += new_char

print(encoded_message)
