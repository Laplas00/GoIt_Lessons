def input_error(func):
    # Decorator
    def wrapper(a):
        print("| Start")
        try:
            result = func(a)
            return result
        except TypeError:
            print('| Type Error')
        except IndexError:
            print('| Index Error')
        except KeyError:
            print('| Key Error')
        finally:
            print('| End')
    return wrapper


@input_error
def add_contact(string):
    contact[string[0]] = string[1]


@input_error
def change(string):
    contact[string[0]] = string[1]


@input_error
def phone(string):
    print(contact[string[0]])





def main():

    commands = {
        'add': add_contact,
        'change': change,
        'phone': phone,
    }

    break_commands = [
        'break', 'quit', 'stop',
        'exit', 'good bye', 'close', 'q'
    ]

    print("\n{:_^50}\n|".format('CACTUS'))
    process = True
    while process:
        sentence = input("|-- ").lower().strip()
        command = sentence.split()

        if sentence == "":
            continue
        elif sentence in break_commands:
            print('| Goog bye')
            process = False

        elif sentence == "hello":
            print("| How can i help u?")

        elif sentence == "show all":
            for i in contact:
                print(i, contact[i])

        elif command[0] in commands:
            commands[command[0]](command[1:])

        else:
            print("| I don't know this command\n| Pls try again")


if __name__ == "__main__":
    contact = {
        'bogdan': '380963031892'
    }
    main()
