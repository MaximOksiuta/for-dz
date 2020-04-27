from itertools import cycle, count

number = int(input('Введите число: '))
string = input('Введите слово: ')
for i in count(number):
    print(i)
    if i > 20:
        break
c = 0
for i in cycle(string):
    print(i)
    if c > 20:
        break
    c += 1
