
import time


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f'{fname} took {after-before} seconds to execute')
        return value

    return wrapper


@timed
def add(x):
    result = 1
    for i in range(x):
        result *= i
    return result


add(678)
