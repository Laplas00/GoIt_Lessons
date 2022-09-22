import re

ola = "My dear friend PLS DIE"


def test():
    start, end = 0, 22
    my_word = ola.find("PLS", start, end)
    my_word = ola.find("PLS")
    print(len(ola))
    print(ola[my_word:])


def string_test(sentence):
    print(sentence.index("a"))
    for i in sentence:
        print(sentence.index(i), " - ", i)


def translatc(message):
    alphabet = {ord('п'): "p", ord("р"): "r", ord("и"): "i",
                ord("в"): "v", ord("е"): "e", ord("т"): "t"}
    ola = message.translate(alphabet)
    print(ola)
    print(alphabet)


def metalang(num):
    if type(num) != int:
        return "False"
    for i in range(num):
        s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
        print(s)


def beaty(first, second, third):
    print("|{:<10}|{:^10}|{:>10}|".format(first, second, third))


print(translatc('привет'))
# print(beaty('ты', "просто", "pidor"))


# numbers = {"UA": [],
#            "JP": ["ola"],
#            "TW": [],
#            "SG": []}

# mine = "38096"
# print(numbers["JP"])
# numbers["JP"].append(mine)
# print(numbers["JP"])


def find_all_links(text):

    result = []
    iterator = re.finditer(
        r"[https:\/\/]{7,8}\w{3}\.?\w{1,}.{1}\w{3}", text)
    for match in iterator:
        result.append(match.group())
    return result
