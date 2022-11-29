
def real_len(text):
    sentenses = ""
    symbols = ['\n', '\f', '\r', '\t', '\v']
    for i in text:
        if i in symbols:
            continue
        else:
            sentenses += i

        print(i, '-')
    print(sentenses)


real_len('Alex\nKdfe23\t\f\v.\r')
