def devider(n_1, n_2):
    try:
        return round(n_1 / n_2, 3)
    except ZeroDivisionError:
        print('Делить на ноль нельзя!!!')
        return ''


try:
    print(devider(int(input('Введите делимое: ')), int(input('Введите делитель: '))))
except ValueError:
    print('Введите число!!!')