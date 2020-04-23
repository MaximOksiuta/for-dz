def splitter(u_str):
    u_str = u_str.split()
    for i in range(0, len(u_str)):
        u_str[i] = int(u_str[i])

    return u_str


def summer(u_str):
    result = sum(u_str)
    print(result)
    return result


itog_sum = 0
while True:
    u_str = input("Для сложения введите числа через пробел для выхода введите 'Q' ")
    if u_str[len(u_str) - 1].upper() == 'Q':
        try:
            u_str = splitter(u_str[:-1])
        except ValueError:
            print('Введите число!!!')
        itog_sum += summer(u_str)
        print(f'Общая сумма - {itog_sum}')
        break
    try:
        u_str = splitter(u_str)
    except ValueError:
        print('Введите число!!!')
    try:
        itog_sum += summer(u_str)
    except ValueError:
        pass
    print(f'Общая сумма - {itog_sum}')