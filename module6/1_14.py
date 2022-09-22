

def total_salary(path):
    sum = 0
    file = open(path, "r")
    file.seek(0)
    while True:
        line = file.readline()
        if len(line) == 0:
            print('break')
            break
        line = line.rstrip()
        num = line[-4:]
        print(num)
        print(int(num))
        num = int(num)
        sum += num

    return sum


print(total_salary("/Users/black/Documents/GoIt_Lessons/module6/train/zarplata.txt"))
