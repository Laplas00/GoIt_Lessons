from core import *


adress_book = AdressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return True

        except UnboundLocalError:
            return False

        except AttributeError:
            return False

        except ValueError:
            return False

        except IndexError:
            return False

        except KeyError:
            print('| key error')
            return False
    return wrapper


@input_error
def add_contact(string):
    string = string.split()
    if len(string) == 3:
        record = Record(string[0], string[1], string[2])
        adress_book.add_record(record)
        return True

    else:
        record = Record(in_name=string[0], in_phone=string[1])
        adress_book.add_record(record)
        return True


@input_error
def add_phone(string):
    name, phone = string.split()
    adress_book[name].add_phone(phone)
    return True


@input_error
def change_phone(string):
    string = string.split()
    record = adress_book.data[string[0]]
    record.change(string[1], string[2])
    return True


@input_error
def show_person(string):
    person = adress_book.data[string]
    for i in adress_book.data[string].phones:
        print(f'- {i.value}')

    if person.brt.value != None:
        print(person.brt.value)

    return True


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


@input_error
def add_brt(string):
    string = string.split(' ')
    name, brt_date = string[0], string[1]
    adress_book.data[name].add_birthday(brt_date)

    return True


@input_error
def days_to_birthday(string):
    if adress_book.in_data(string):
        if adress_book.data[string].brt.value == None:
            return f'{string} have no birthday'
        record = adress_book[string]
        print('start')
        print(adress_book.days_to_birthday(record))
        return True


#  =========   Pickle data  =========   #

def save_data():
    with open('data.bin', 'wb') as file_in:
        pickle.dump(adress_book.data, file_in)


def unpacking_data():
    with open('data.bin', 'rb') as file_out:
        return pickle.load(file_out)

#  =========   Pickle data  =========   #


@input_error
def all_notes(count):
    count = int(count)
    adress_book.iteration(count)

    for _ in range(count):
        print(next(adress_book))

#################################
#             test              #


add_contact('bogdan 39084')
add_phone('bogdan 45555')
add_phone('bogdan 44444')
add_phone('bogdan 33333')
add_phone('bogdan 22222')
add_phone('bogdan 00000')
add_brt('bogdan 03.09.2002')

add_contact('maks lopata')
add_phone('maks kuskus')
add_phone('maks luci')
add_phone('maks manka')
add_phone('maks oplet')
add_phone('maks dibil')

add_contact('sasha pupsik 14.08.2003')
add_phone('sasha love')


##################################

COMMANDS = {
    'add':  add_contact,
    'remove':  remove,
    'add phone': add_phone,
    'show': show_person,
    'change': change_phone,
    'all': all_notes,
    'add birthday': add_brt,
    'days to birthday': days_to_birthday,
    'show all': None
}


def main():

    adress_book.data = unpacking_data()

    print(
        '> Hello user\nI have this commands:\n')
    print(
        '-add [name phone* dd.mm.yyyy*]\n-add phone [name phone]\n-add birthday [name birthday]')
    print('\n-change[name phone new_phone]\n-remove[name phone]')
    print(
        '\n-show [name]\n-show all\n-all [num of notes]\n-days to birthday [name]')
    print("\n * - optional field\n[..] - args to command")

    while True:
        u_input = input('∞ ').rstrip().lstrip()

        if u_input in ['bye', 'quit', 'exit', 'break', 'q']:
            print('> Bye :)')
            break

        if u_input in ['hello',  'hey']:
            print('> Welcome my lord')

            for i in COMMANDS:
                print(f'-{i}')

        elif u_input == 'show all':
            print(adress_book.data)

        elif u_input == 'clear':
            system('clear')

        elif u_input == 'save data':
            save_data()

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
