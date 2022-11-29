

from concurrent.futures import BrokenExecutor


grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students):
    mylist = []
    id = 0
    for name, ball in students.items():
        print(name, ball)
        if id == len(students)+1:
            print('here')
            return "stop"
        else:

            line = ("{:>4}|{:<10}|{:^5}|{:^5}".format(
                id+1, name, ball, grades[ball]))
            id += 1
            mylist.append(line)

    return mylist


# print(formatted_grades(students))
for i in formatted_grades(students):
    print(i)
