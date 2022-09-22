from random import randint


def get_passwd():
    passwd = ""
    for i in range(8):
        a = randint(40, 126)
        passwd += chr(a)
    return passwd


print(get_passwd())
