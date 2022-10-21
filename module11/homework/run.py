from core import *
from os import system

adress_book = AdressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return True
        except (ValueError, IndexError, UnboundLocalError):
            return False
        except KeyError:
            return False
    return wrapper


@input_error
def add_contact(string):
    string = string.split()
    record = Record(string[0], string[1])
    adress_book.add_record(record)
    return True


@input_error
def add_phone(string):
    string = string.split()
    adress_book[string[0]].phones.append(Phone(string[1]))
    return True


@input_error
def change_phone(string):
    string = string.split()
    record = adress_book.data[string[0]]
    record.change(string[1], string[2])
    return True


@input_error
def show_person(string):
    string = string.split()
    name = string[0]
    for i in adress_book.data[name].phones:
        print(i.value)


@input_error
def remove(string):
    string = string.split()
    name, phone = string[0], string[1]
    if adress_book.in_data(name) != True:
        return False

    for i in adress_book.data[name].phones:
        if i.value == phone:
            record = adress_book[name]
            record.remove_phone(phone)
            return True

    return False


COMMANDS = {
    'add':  add_contact,
    'remove':  remove,
    'add phone': add_phone,
    'show': show_person,
    'change': change_phone,
}


add_contact('bogdan 39084')
add_phone('bogdan 45555')
add_phone('bogdan 44444')
add_phone('bogdan 33333')
add_phone('bogdan 22222')
add_phone('bogdan 00000')

add_contact('maks lopata')
add_phone('maks kuskus')
add_phone('maks luci')
add_phone('maks manka')
add_phone('maks oplet')
add_phone('maks dibil')


def main():
    print('> Hello user\nI have this commands:')
    print('-add [name phone]\n-change [name phone new_phone]\n-remove [name phone]')
    print('-add phone [name phone]\n-show [name]\n-show all')

    while True:
        u_input = input('∞ ').rstrip().lstrip()

        if u_input in ['bye', 'quit', 'exit', 'break', 'q']:
            print('> Bye :)')
            break

        if u_input in ['hello',  'hey']:
            print('> Welcome my lord')
            print('> How can i halp u?')

        elif u_input == 'show all':
            page = 4

            print(adress_book.iteration(page))

        elif u_input == 'clear':
            system('clear')

        elif u_input in COMMANDS:
            string = input('Command args: ')
            command = COMMANDS[u_input]
            if command(string) == True:
                print('> Done!')

            else:
                print('> Check again args  to this command!')

        else:
            print('> I cant find this')


if __name__ == "__main__":
    main()
