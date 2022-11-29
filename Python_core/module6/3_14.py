

def read_employees_from_file(path):
    file = open(path, "r")
    my = []
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        my.append(line.rstrip())

    file.close()
    return my


print(read_employees_from_file(
    "/Users/black/Documents/GoIt_Lessons/module6/train/rabotniki.txt"))
