class OINTError(Exception):
    pass


def adder(number, ls):
    try:
        if number.isdigit():
            ls.append(number)
        else:
            raise OINTError
    except OINTError:
        print('В список можно добавлять только число!!!')


u_list = []
while True:
    u_number = input(f'Введите число которое вы хотите добавить в список\n{u_list}\nдля выхода нажмите Enter: ')
    if u_number == '':
        break
    adder(u_number, u_list)
