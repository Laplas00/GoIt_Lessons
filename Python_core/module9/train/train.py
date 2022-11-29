import os


def clear():
    os.system('clear')


result = []


def add_contact(string):
    print("here the add")
    result.append(string)
    print(result)
    return 'Yep its worrk'


commands = {
    'add': add_contact,
    'clear': clear
}


def get_handdler(comand):
    return commands[comand]


process = True
while process:
    comand = input('впиши команду ').lower()
    words = comand.split()
    print(words)
    if words[0] not in commands:
        print('такого нет\nЕще раз пожалуйста')
        continue
    else:
        handler = get_handdler(words[0])
        handler(comand)
