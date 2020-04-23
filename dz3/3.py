def summer(a, b, c):
    ls = [a, b, c]
    ls.remove(min(ls))
    return sum(ls)


try:
    a = int(input('Введите 1 число: '))
    b = int(input('Введите 2 число: '))
    c = int(input('Введите 3 число: '))
    print(f'{summer(a, b, c)} - сумма 2 наибольших чисел')
except ValueError:
    print('Введите число!!!')