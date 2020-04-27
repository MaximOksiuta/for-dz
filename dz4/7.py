from itertools import count


def fibo_gen(n):
    for en in count(1):
        if en > n:
            break
        yield en


i = 0
result = 1
for en in fibo_gen(int(input('Введите число факториал которого хотите получить: '))):
    if i == 15:
        break
    i += 1
    print(en)
    result *= en
print(f'Факториал вашего числа - {result}')
