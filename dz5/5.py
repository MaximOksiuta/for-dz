from random import randrange
from functools import reduce
with open("text_5.txt", 'a', encoding='utf-8') as text:
    for number in [f'{randrange(0,100)} ' for i in range(0,100)]:
        text.write(number)
with open("text_5.txt", 'r', encoding='utf-8') as text:
    for i in text.readlines():
        try:
            result = reduce((lambda a, b: int(a)+int(b)), i.split())
            print(f'{result} - сумма всех чисел в файле')
        except ValueError:
            print('В файле есть не только числа!!!')
