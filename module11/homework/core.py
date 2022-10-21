from collections import UserDict

# All my classes


class Field:
    pass


class Iteration(UserDict):
    N = 4

    def __init__(self):

        self.cur = 0

    def __next__(self):
        print('next')
        if self.cur < self.N:
            print('<<')
            self.cur += 1
            return self.cur
        raise StopIteration


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone


class AdressBook(UserDict):
    N = 3
    all_values = []

    def in_data(self, name):
        if name in self.data:
            return True
        return False

    def add_record(self, record):
        self.data[record.name.value] = record

    def show_all(self):
        print(self.data)

    def iteration(self, count):

        print('v iter')
        self.N = count

        for i in self.data:
            for di in self.data[i].phones:
                self.all_values.append(di)

        book = (x.value for x in self.all_values)

        for i in book:
            print(i)

        # for name, keys in self.data.items():
        #     for value in keys.phones:
        #         print(value.value)
        # return 'Done'


class Record(Field):
    def __init__(self, in_name, in_phone=None):
        self.now = 0
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

    def __next__(self):
        print('0123123123123123123123123123123123')
        yield self

    # def __next__(self):
    #     print('NEEEEEXT')
    #     if self.now < self.N:
    #         self.now += 1
    #         return self.now
    #     else:
    #         return StopIteration
