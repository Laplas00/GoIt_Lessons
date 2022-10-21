from collections import UserDict

# All my classes


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone


class AdressBook(UserDict):
    N = 0
    cur = 0
    all_values = []

    def __init__(self):
        super().__init__()
        self.book = []

    def in_data(self, name):
        if name in self.data:
            return True
        return False

    def add_record(self, record):
        self.data[record.name.value] = record

    def iteration(self, count):
        self.N += count

        for name, value in self.data.items():
            for value in self.data[name].phones:
                self.book.append(value.value)

    def __next__(self):
        if self.cur < self.N:
            self.cur += 1
            return self.book[self.cur]
        else:
            raise StopIteration


class Record(Field):

    def __init__(self, in_name, in_phone=None):
        self.cur = 0
        self.N = 3
        self.name = Name(in_name)
        self.phones = []
        if in_phone != None:
            self.phones.append(Phone(in_phone))

    def add_phone(self, phone=None):
        self.phones.append(Phone(phone))

    def change(self, old_note, new_note):
        for old in self.phones:
            if old.value == old_note:
                self.phones.remove(old)
                self.phones.append(Phone(new_note))

    def remove_phone(self, phone):
        for old in self.phones:
            if old.value == phone:
                self.phones.remove(old)
