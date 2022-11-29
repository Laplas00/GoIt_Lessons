# Practiucal example Login


def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            f.write(f'{fname} returned value {value}\n')
            print(f'{fname} returned value {value}')
        return value
    return wrapper


@logged
def add(x, y):
    return x+y


print(add(10, 20))
