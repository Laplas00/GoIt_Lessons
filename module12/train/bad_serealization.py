
contacts = {'bogdan': '222',
            'sasha': '333'
            }


def add_contact(name, phone):
    contacts[name] = phone
    return 'Done'


with open('contacts.txt', 'w') as file_in:
    for key, value in contacts.items():
        file_in.writelines(f'{key}|{value}\n')
