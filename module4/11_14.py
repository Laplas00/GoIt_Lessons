def is_valid_password(password):
    if len(password) < 8:
        return False
    nums = "012345678"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if set(password) & set(nums):
        print('yes ?')
        if set(password) & set(alphabet):
            print('really ?')
            if set(password) & set(upal):
                print("oooo yeeeee")
                return True
            else:
                return False
        else:
            return False
    else:
        return False


is_valid_password('NmlDl1V0')
