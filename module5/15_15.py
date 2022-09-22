import re


def find_all_links(text):
    pattern = r"\https?://[a-z]{2,}.?[a-z]{1,}.[a-z]{3}"
    result = []
    iterator = re.finditer(pattern, text)
    for match in iterator:
        result.append(match.group())
    return result


text = """
Функция find_all_links возвращает неправильный результат: 

['https://www.google.com', 'https://www.facebook.com', 
'http://github.com', 'https://www..facebook.com']. 

Ожидалось, что функция find_all_links при получении параметра

 'The main search site in the world is https://www.google.com 
 The main social network for people in the world is 
 https://www.facebook.com But programmers have their own 
 social network http://github.com There they share their code.
  some url to check https://www..facebook.com www.facebook.com '

 вернет следующий список 

['https://www.google.com', 'https://www.facebook.com', 'http://github.com']
"""

print(find_all_links(text))
