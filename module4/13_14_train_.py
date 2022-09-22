from genericpath import isdir
from pathlib import Path
import os

# /Users/black/Documents/surprize


def my_minitry():
    """ Тут я хотел совместить os.system c тем что выдает pathlib

    У меня не вышло, но я думаю я просто не до конца
    решил это, поэтому оставлю это тут в виде функции
    """
    p = Path('/Users/black/Documents/surprize')
    l = [print(x, "ola") for x in p.iterdir()]
    print("=-=-=-=-=-=-=")

    for i in p.iterdir():

        la = str(i)
        nf = la.split('/')
        nf = nf[-1]

        print(nf, " there is a need file")
        if la[-3:] == "mzf":
            print("here")
            ola = "cat "
            ola += nf
            os.system(f"ola {nf}")


def parse_folder(path):
    p = Path(path)
    files = []
    folders = []
    for i in p.iterdir():
        print(i.name, "its a file's name")
        if i.is_dir() == True:
            folders.append(i.name)
            transform = str(i)
            transform = transform.split('/')
            print(f"{transform[-1]} is a directory")
        elif i.is_file() is True:
            files.append(i.name)
            transform = str(i)
            transform = transform.split('/')
            print(f"{transform[-1]} p.is_file")
        else:
            print('no wa')


my_minitry("/Users/black/Documents/surprize")
