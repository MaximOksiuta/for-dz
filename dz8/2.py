class ZDEVError(Exception):
    pass


def dev(a, b):
    try:
        if b == 0:
            raise ZDEVError
        return a/b
    except ZDEVError:
        print('Делить на ноль нельзя!!!')
    except ZeroDivisionError:
        pass


while True:
    try:
        dividend =input('Для выхода нажмите Enter или введите делимое:')
        if dividend == '':
            break
        else:
            dividend = int(dividend)
            divider = int(input('Делитель: '))
            print(dev(dividend, divider))
    except ValueError:
        print('Делимиое и делитель это числа!!')