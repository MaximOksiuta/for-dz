from random import randint


class Warehouse:
    def __init__(self, name='удалённый', c_printer=0, c_scanner=0, c_xerox=0, shop=False):
        self.name = name
        self.printer = Printer(c_printer)
        self.scanner = Scanner(c_scanner)
        self.xerox = Xerox(c_xerox)
        self.shop = shop
        self.things = {'printer': self.printer, 'scanner': self.scanner, 'xerox': self.xerox}
        if name == 'удалённый':
            print('Удалённый склад построен')
        else:
            print(f'Склад в {name} построен')

    def __str__(self):
        return f'{self.name} - {self.printer.count} принтеров, {self.scanner.count} сканеров, ' \
               f'{self.xerox.count} ксераксов'


class Org_tesh:
    warehouses = []


class Printer(Org_tesh):
    def __init__(self, count):
        self.count = count
    price = 20000


class Scanner(Org_tesh):
    def __init__(self, count):
        self.count = count
    price = 5000


class Xerox(Org_tesh):
    def __init__(self, count):
        self.count = count
    price = 30000


ot = Org_tesh()
try:
    with open('save.txt', 'r', encoding='utf-8') as f:
        content = f.readline()
        ls = content.split('/')
except FileNotFoundError:
    wh = Warehouse()
    ot.warehouses.append(wh)
    money = 7000000
else:
    if input('Найдено сохранение загрузить (да/нет)?  ') == 'да':
        for n in range(0, len(ls) // 5):
            cont_ls = []
            for i in ls[5 * n:5 * n + 5]:
                cont_ls.append(i)
            ot.warehouses.append(
                Warehouse(cont_ls[1], cont_ls[2], cont_ls[3], cont_ls[4], cont_ls[0]))
        money = ls.pop()
    else:
        wh = Warehouse()
        ot.warehouses.append(wh)
        money = 7000000
while True:
    user_str = input('Выберите действие\nдля открытия памятки введите "help"\nдля выхода введите "Q"  ')
    if user_str.lower() == 'help':
        n = 0
        print()
        print(f'У вас {money} рублей')
        print(f'принтер стоит 20000 рублей, сканер стоит 5000 рублей, а ксерокс стоит 30000 рублей')
        for i in ot.warehouses:
            n += 1
            print(f'перейти в склад {i.name} - {n}')
        n += 1
        print()
        print(f'Строительство нового склада - {n}')
        print()

    elif user_str.upper() == 'Q':
        with open('save.txt', 'w', encoding='utf-8') as f:
            f.write("")
        with open('save.txt', 'a', encoding='utf-8') as f:
            for i in ot.warehouses:
                f.write(f'{i.shop}/')
                f.write(f'{i.name}/')
                f.write(f'{str(i.things["printer"].count)}/')
                f.write(f'{str(i.things["scanner"].count)}/')
                f.write(f'{str(i.things["xerox"].count)}/')
            f.write(str(money))
        break
    elif user_str.isdigit() and int(user_str) <= len(ot.warehouses):
        number = int(user_str) - 1
        while True:
            print(f'Вы перешли в склад {ot.warehouses[number].name}\n{ot.warehouses[number]}')
            user_command = input('Выберите действие\nдля открытия памятки введите "help"\nдля выхода введите "Q"  ')
            if user_command.lower() == 'help':
                n = 0
                for i in ot.warehouses:
                    n += 1
                    if i.name != ot.warehouses[number].name:
                        print(f'Отправить технику на склад - {i.name} - {n}')
                print()
                n += 1
                print(f'Купить технику - {n}')
                n += 1
                print(f'Продать технику - {n}')
                n += 1
                if ot.warehouses[number].shop or ot.warehouses[number].name == 'удалённый':
                    print(f'Разрушить склад - {n+1}')
                else:
                    print(f'Построить магазин в {ot.warehouses[number].name} - {n}')
                    n += 1
                    print(f'Разрушить склад - {n}')
            elif user_command.upper() == 'Q':
                break
            elif user_command.isdigit() and int(user_command) <= len(ot.warehouses):
                c_number = int(user_command) - 1
                tesh_type = input(f'Какой тип техники вы хотите отправить на склад - {ot.warehouses[c_number].name}\n'
                                  f'printer - 1\nscanner - 2\nxerox - 3\nотмена - "Q"  ')

                if tesh_type.upper() == 'Q':
                    pass
                else:
                    try:
                        if tesh_type.isdigit():
                            tesh_type = int(tesh_type)
                            try:
                                ht = int(input('Сколько шт.?  '))
                            except TypeError:
                                print('Колличество это число!!!')
                            text_type = 'printer' if tesh_type == 1 else 'scanner' if tesh_type == 2 else 'xerox'
                            if ot.warehouses[number].things[text_type].count < ht:
                                print(f'На данном складе только {ot.warehouses[number].things[text_type].count} '
                                      f'{"принтеров" if tesh_type == 1 else "сканеров" if tesh_type == 2 else "ксероксов"}')
                            else:
                                go_price = (2 if tesh_type == 1 else 1 if tesh_type == 2 else 3)*ht*1000
                                if input(f'Отправка {ht} '
                                         f'{"принтеров" if tesh_type == 1 else "сканеров" if tesh_type == 2 else "ксероксов"}'
                                         f' на склад {ot.warehouses[c_number].name} будет стоить {go_price} рублей продолжить?'
                                         f'(да/нет)?  ') == 'да':
                                    ot.warehouses[number].things[text_type].count -= ht
                                    if randint(0, 100) == 2:
                                        money -= go_price//2
                                        print('Грузовая машина попала в аврию.')
                                        print(f'Груз утерян, транспортная компания согласилась вернуть только 50% '
                                              f'стоимости перевозки.\nДенег осталось {money} рублей')
                                    else:
                                        ot.warehouses[c_number].things[text_type].count += ht
                                        money -= go_price
                                        print(f'Техника прибала на склад {ot.warehouses[c_number].name}, '
                                              f'денег осталось: {money} рублей')
                    except ValueError:
                        print('Command not found')
            elif user_command.isdigit() and int(user_command) == len(ot.warehouses) + 1:
                tesh_type = input(f'Введите тип техники который вы хотите закупить на склад - '
                                  f'{ot.warehouses[number].name}\n'
                                  f'printer - 1\nscanner - 2\nxerox - 3\nотмена - "Q"  ')
                if tesh_type.upper() == 'Q':
                    pass
                else:
                    try:
                        if tesh_type.isdigit():
                            if ot.warehouses[number].name == 'удалённый':
                                if input(f'Техника будет закуплена на склад {ot.warehouses[0].name} '
                                         f'продолжить (да/нет)?  ') == 'да':
                                    try:
                                        ht = int(input('Сколько шт.?  '))
                                    except ValueError:
                                        print('Колличество это число!!!')
                                    tesh_type = int(tesh_type)
                                    text_type = 'printer' if tesh_type == 1 else 'scanner' if tesh_type == 2 else 'xerox'
                                    if money < ot.warehouses[number].things[text_type].price * ht:
                                        print(f'Недостаточно средств\nу вас {money} рублей, а {ht} '
                                              f'{"принтеров" if tesh_type == 1 else "сканеров" if tesh_type == 2 else "ксераксов"}'
                                              f' стоят {ot.warehouses[number].things[text_type].price * ht} рублей')
                                    else:
                                        money -= ot.warehouses[number].things[text_type].price * ht
                                        ot.warehouses[number].things[text_type].count += ht
                                        print(f'Было закуплено {ht} '
                                              f'{"принтеров" if tesh_type == 1 else "сканеров" if tesh_type == 2 else "ксераксов"} '
                                              f'денег осталось {money} рублей')
                            else:
                                if input(f'Техника будет закуплена на склад {ot.warehouses[0].name} '
                                         f'и автоматически перевезена на склад {ot.warehouses[number].name} '
                                         f'продолжить (да/нет)?  ') == 'да':
                                    try:
                                        ht = int(input('Сколько шт.?  '))
                                    except ValueError:
                                        print('Колличество это число!!!')
                                    tesh_type = int(tesh_type)
                                    text_type = 'printer' if tesh_type == 1 else 'scanner' if tesh_type == 2 else 'xerox'
                                    if money < ot.warehouses[number].things[text_type].price * ht:
                                        print(f'Недостаточно средств\nу вас {money} рублей, а {ht} '
                                              f'{"принтеров" if tesh_type == 1 else "сканеров" if tesh_type == 2 else "ксераксов"}'
                                              f' стоят {ot.warehouses[number].things[text_type].price * ht} рублей')
                                    else:
                                        money -= ot.warehouses[number].things[text_type].price * ht
                                        go_price = (2 if tesh_type == 1 else 1 if tesh_type == 2 else 3) * ht * 1000
                                        if money < go_price:
                                            ot.warehouses[0].things[text_type].count += ht
                                            print(f'Было закуплено {ht} '
                                                  f'{"принтеров" if tesh_type == 1 else "сканеров" if tesh_type == 2 else "ксераксов"} ')
                                            print(f'Техника была закуплена на склад {ot.warehouses[0].name}, '
                                                  f'но для её перевозки на склад {ot.warehouses[number].name} '
                                                  f'недостаточно средств\nДенег осталось {money} рублей')
                                        else:
                                            money -= go_price
                                            if randint(0, 100) == 2:
                                                money += (go_price/2)
                                                print('Грузовая машина попала в аврию.')
                                                print(f'Груз утерян, транспортная компания согласилась '
                                                      f'вернуть только 50% '
                                                      f'стоимости перевозки.\nДенег осталось {money} рублей')
                                            else:
                                                ot.warehouses[number].things[text_type].count += ht
                                                print(f'Было закуплено {ht} '
                                                      f'{"принтеров" if tesh_type == 1 else "сканеров" if tesh_type == 2 else "ксераксов"} '
                                                      f'денег осталось {money} рублей')
                    except TypeError:
                        print('Command not found')
            elif user_command.isdigit() and int(user_command) == len(ot.warehouses) + 2:
                tesh_type = input(f'Введите тип техники вы хотите продать со склада - {ot.warehouses[number].name}\n'
                                  f'printer - 1\nscanner - 2\nxerox - 3\nотмена - "Q"   ')
                if tesh_type.upper() == 'Q':
                    pass
                else:
                    try:
                        if tesh_type.isdigit():
                            if input('Техника будет автоматически направлена в магазин'
                                     ' и продана продолжить (да/нет)') == 'да':
                                if ot.warehouses[number].name == 'удалённый':
                                    print(f'Продавать что либо с удалённого склада нельзя\n'
                                          f'Для продажи техники отправьте её в другой склад')
                                else:
                                    if ot.warehouses[number].shop:
                                        try:
                                            ht = int(input('Сколько шт.?  '))
                                        except TypeError:
                                            print('Колличество это число!!!')
                                        tesh_type = int(tesh_type)
                                        text_type = 'printer' if tesh_type == 1 else 'scanner' if tesh_type == 2 else 'xerox'
                                        if ot.warehouses[number].things[text_type].count < ht:
                                            print(f'На данном складе только {ot.warehouses[number].things[text_type].count} '
                                                  f'{"принтеров" if tesh_type == 1 else "сканеров" if tesh_type == 2 else "ксероксов"}')
                                        else:
                                            money += (ot.warehouses[number].things[text_type].price +
                                                      (3000 if tesh_type == 2 else 5000 if tesh_type == 1 else 10000))\
                                                     * ht
                                            ot.warehouses[number].things[text_type].count -= ht
                                            print(f'Было продано {ht} '
                                                  f'{"принтеров" if tesh_type == 1 else "сканеров" if tesh_type == 2 else "ксераксов"} '
                                                  f'денег стало - {money}')
                                    else:
                                        print(f'У вас нет магазина в {ot.warehouses[number].name}')
                    except TypeError:
                        print('Command not found')
            elif user_command.isdigit() and int(user_command) == len(ot.warehouses) + 3:
                if ot.warehouses[number].name == 'удалённый':
                    print('Построить магазин для удалённого склада нельзя')
                else:
                    if ot.warehouses[number].shop == False and input('Строительство магазина стоит 1000000 рублей продолжить'
                                                                     ' (да/нет)?  ').lower() == "да":
                        if money < 1000000:
                            print(f'У вас только {money} рублей')
                        else:
                            money -= 1000000
                            ot.warehouses[number].shop = True
                            print(f'Магазин в {ot.warehouses[number].name} построен.\n'
                                  f'Денег осталось {money} рублей')
            elif user_command.isdigit() and int(user_command) == len(ot.warehouses) + 4:
                if input('Уничтожение склада продолжить (да/нет)?  ').lower() == "да":
                    ot.warehouses.pop(number)
                    break
    elif user_str.isdigit() and int(user_str) <= len(ot.warehouses) + 1:
        if input('Строительство склада стоит 5 млн. рублей продолжить (да/нет)?  ').lower() == "да":
            if money < 5000000:
                print('Недостаточно средств')
            else:
                ot.warehouses.append(Warehouse(input('В каком городе вы хотите построить склад?  ')))
                money -= 5000000
                print(f'У вас осталось {money} рублей')
