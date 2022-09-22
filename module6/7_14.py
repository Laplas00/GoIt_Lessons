import re


def sanitize_file(source, output):
    pattern = r"\D{1,}"
    with open(source, "r") as file:
        lol = file.read()
        without = re.findall(pattern, lol)
        without = "".join(without)
        with open(output, "w") as output:
            output.write(without)


print(sanitize_file("/Users/black/Documents/GoIt_Lessons/module6/train/recipies.txt",
      "/Users/black/Documents/GoIt_Lessons/module6/train/bezcifr.txt"))
