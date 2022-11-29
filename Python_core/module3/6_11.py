def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        print(string+" /// ")
        spaces = (length - len(string)) // 2
        print(spaces)
        return ("["+string + ("." * spaces)+"]")


print(format_string(length=15, string='abaa'))
