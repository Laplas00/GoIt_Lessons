import re
from pathlib import Path
import os
import sys
import shutil


TRANS = {ord('а'): 'a', ord("б"): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): "e", ord('ё'): "e", ord('ж'): "j", ord('з'): "z", ord('и'): "i", ord('й'): "y", ord('к'): "k", ord('л'): "l", ord('м'): "m", ord('н'): "n", ord('о'): "o", ord('п'): "p", ord('р'): "r", ord('с'): "c", ord('т'): "t", ord('у'): "u",
         ord('ф'): "f", ord('х'): "x", ord('ц'): "ts", ord('ч'): "ch", ord('ш'): "sh", ord('щ'): "sch", ord('ъ'): "", ord('ы'): "y", ord('ь'): "", ord('э'): "e", ord('ю'): "yu", ord('я'): "ya", ord('є'): "ye", ord('і'): "i", ord('ї'): "yi", ord('ґ'): "g"}

folders = {'images': ['png', 'jpg', 'jpeg', 'svg'],
           'video': ['mp4', 'mov', 'mkv', 'avi'],
           'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
           'audio': ['mp3', 'ogg', 'wav', 'amr'],
           'archives': ['zip', 'gz', 'tar']


           }


def normalize(string):

    result = ''

    name = string.split('.')
    ext = name.pop(-1).lower()
    name = '_'.join(name)
    name = name.lower()
    name = name.translate(TRANS)

    some = re.findall(r'[a-zA-Z0-9]', name)

    for i in name:
        if i not in some:
            result += '_'
            continue
        else:
            result += i
    result = result + '.' + ext
    namedir = os.path.dirname(string)
    new_filepath = os.path.join(namedir, result)
    if str(string) == str(new_filepath):
        print("| No need changes")
        print("|{}".format("-"*50))

        return new_filepath
    else:
        print("| New name is", os.path.basename(new_filepath))
        print("| New name is", os.path.basename(string))
        print(f'| Result is - {result}')
        print(f'| String is - {string}')
        print(os.system('pwd'))

        os.rename(string,  result)
        return new_filepath


def move_to_folder(filepath):
    print(filepath, 111)
    file_p = Path(filepath)
    file = file_p.name
    if os.path.basename(file).startswith(".DS"):
        print(
            f"| ------- {os.path.basename(file)} ------- DELETE  КУСОК ГОВНА")
        os.remove(file)

    elif os.path.basename(file).startswith(".ds"):
        print(
            f"| ------- {os.path.basename(file)} ------- DELETE  КУСОК ГОВНА")
        os.remove(file)

    print(f'FILE IN MTF IS  ---- {file}')
    full_path = os.path.join(DIRECTORY, file)

    ext = file.split('.')[-1]
    for key in folders:

        if ext in folders[key]:
            need_path = os.path.join(DIRECTORY, key)

            print(f'NEED PATH IS {need_path}')

            if key in os.listdir(DIRECTORY):
                print(os.listdir(DIRECTORY))
                print('\n\n\n')
                shutil.move(full_path, filepath)

            else:
                os.mkdir(need_path)
                shutil.move(full_path, file)

        else:
            print('shît')


def sort(path):
    print(f'My folder now is  - {path}')
    os.chdir(path)
    path = Path(path)

###         Dir recursion       ###

    for file in path.iterdir():

        print(f'File is - {file}')
        if file.is_dir():
            print(f'| {file.name} - is  directory')

            if len(os.listdir(file)) == 0:
                print(f'{file} is empty\nDeliting')
                os.rmdir(file)
                break

            if file.name in folders.keys():
                print('this  file not for sort')
                continue

            print('\n\t\tRECURSION\n\n')
            sort(file)

        else:
            print('GBALE')

###         File sorting           ###

        if file.exists() != True:
            print('zopa', file)
            print('\n\t\tEXIT RECURSION\n\n')
            break

        elif file.is_file():
            filename = file.name
            res = normalize(filename)
            move_to_folder(os.path.abspath(res))
            print(f'Res is - {res}')

        else:
            print('\n\nELSELSELSELSELSELSELSEL\n\n')
            break


if __name__ == '__main__':
    DIRECTORY = sys.argv[1]
    sort(DIRECTORY)
