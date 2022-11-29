import os

from pathlib import Path


folders = {
    'images': ['jpg', 'img', 'png'],
    'audio': ['mp3', 'mp4']
}

res = []
for key, value in folders.items():
    for i in value:
        res.append(i)
print(res)

print('mp4' in res)


def normilize(str):
    result = 'ooo'
    return result
    #   lala.png
    #   ['lala','png']


path = Path('.')
print(path)
os.chdir(path)
print(os.system('pwd'))


def sorting(path):
    for file in path.iterdir():
        if file.is_dir():
            print(f'| {file.name} - is  directory')
            sorting(file)

        elif file.is_file():
            filename = file.name
            res = normilize(filename)
            name, ext = filename.split('.')
            print(f'| Ext is - {ext}\n| Name is - {name}')

            for key in folders:
                if ext in folders[key]:
                    all_files = [x.name for x in path.iterdir()]
                    if key in all_files:
                        print('im Dont  need this shit')
                        # move file
                        continue
                    else:
                        os.mkdir(key)
                        # move file
                        continue


sorting(path)


# def normilize(string):

#     name_parts = string.split('.')
#     print(name_parts)
#     ext = name_parts[-1]


#     name_parts.remove(ext)
#     good_name = '_'.join(name_parts)

#     return good_name+'.'+ext


# print(normilize('pyt.h($.$$)n.jpg'))
