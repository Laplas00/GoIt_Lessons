def get_cats_info(path):
    result = []
    with open(path, "r") as file:
        while True:
            cat = file.readline()
            if len(cat) == 0:
                print('here stope ')
                break
            cat = cat.rstrip().split(',')
            result.append({"id": cat[0], "name": cat[1], "age": cat[2]})

        file.close()
    return result


print(get_cats_info("/Users/black/Documents/GoIt_Lessons/module6/train/cats.txt"))
