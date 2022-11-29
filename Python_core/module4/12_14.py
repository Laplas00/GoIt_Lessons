from random import randint


def get_random_password():
    passwd = ""
    for i in range(8):
        a = randint(40, 126)
        passwd += chr(a)
    return passwd


def is_valid_password(password):
    if len(password) < 8:
        return False
    nums = "012345678"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if set(password) & set(nums):

        if set(password) & set(alphabet):

            if set(password) & set(upal):
                print("Succes")
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def get_password():
    count = 99
    while count != 0:
        count -= 1
        passwd = get_random_password()
        print(f'---  {passwd} --- is our password')
        if is_valid_password(passwd):
            return passwd
        else:
            continue


print(get_password())
