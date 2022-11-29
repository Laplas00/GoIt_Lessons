from itertools import tee
import re

# p = re.sub(r'(blue|white|red)', 'color', 'blue socks and red shoes')
# print(p)  # color socks and color shoes


sentenses = "Privet ti pIdor, gryazniq xyeSos"

bad_words = ["pidor", "xyesos"]

for i in bad_words:

    sentenses = re.sub(i, "*"*len(i), sentenses, flags=re.IGNORECASE)


print(sentenses)


# result = [re.sub(x, "*"*len(x), sentenses) for x in bad_words]

# print(result)
# print(sentenses)

# # print(re.compile(result, flags=0))
