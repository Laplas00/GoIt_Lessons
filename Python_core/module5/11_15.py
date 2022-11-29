import re
from sys import flags

text = """ Guido van Rossum began 
working on PYthon inthe late 1980s, 
as a successor to the ABC programming 
language,and first released it in 1991 
as Python 0.9.0  Python'"""


word = 'Python'

mifind = re.compile(word, re.IGNORECASE)
result = re.findall(word, text, re.IGNORECASE)


print(result)


# def find_all_words(text, word):
#     result = re.findall(word, text, re.IGNORECASE)
#     return result


# print(find_all_words(text, word))
