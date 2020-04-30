from re import findall
from functools import reduce


def numbers_from_string(data):
    result = findall(r'\d+', data)
    return result


dictionary = {}
with open("text_6.txt", 'r', encoding='utf-8') as f:
    content = f.readlines()
    for string in content:
        list = string.split(': ')
        dictionary.update({list[0]:(reduce((lambda a, b: int(a)+int(b)),numbers_from_string(list[1])))})
print(dictionary)