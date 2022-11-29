

def formatted_numbers():
    mylist = []
    line = ('|{:^10}|{:^10}|{:^10}|'.format("decimal", "hex", "binary"))
    mylist.append(line)
    for i in range(16):
        mylist.append("|{:<10d}|{:^10x}|{:>10b}|".format(i, i, i))

    return mylist


for i in formatted_numbers():
    print(i)
