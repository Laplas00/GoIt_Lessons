def write_employees_to_file(employee_list, path):

    file = open(path, "w+")
    for i in employee_list:
        for di in i:
            file.write(f"{di}\n")
    file.close()
    return "done"


rabotniki = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]


print(write_employees_to_file(
    rabotniki, "/Users/black/Documents/GoIt_Lessons/module6/train/rabotniki.txt"))
