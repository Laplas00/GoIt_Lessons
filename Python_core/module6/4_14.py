def add_employee_to_file(record, path):
    file = open(path, "a")
    file.write(f"\n{record}")
    file.close()


add_employee_to_file("Ya suka i mne 14",
                     "/Users/black/Documents/GoIt_Lessons/module6/train/rabotniki.txt")
