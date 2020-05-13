class Warehouse:
    def __init__(self, name='удалённый'):
        self.name = name
        self.printer = Printer()
        self.scanner = Scanner()
        self.xerox = Xerox()
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
    count = 0
    price = 20000


class Scanner(Org_tesh):
    count = 0
    price = 5000


class Xerox(Org_tesh):
    count = 0
    price = 30000


wh = Warehouse()
ot = Org_tesh()
ot.warehouses.append(wh)
money = 6000000
while True:
    user_str = input('Выберите действие\nдля открытия памятки введите "help"\nдля выхода введите "Q"  ')
    if user_str.lower() == 'help':
        n = 0
        print()
        print(f'принтер стоит 20000 рублей, сканер стоит 5000 рублей, а ксерокс стоит 30000 рублей')
        for i in ot.warehouses:
            n += 1
            print(f'перейти в склад {i.name} - {n}')
        n += 1
        print()
        print(f'Строительство нового склада - {n}')
        print()

    elif user_str.upper() == 'Q':
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
                                ot.warehouses[number].things[text_type].count -= ht
                                ot.warehouses[c_number].things[text_type].count += ht
                    except TypeError:
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
                            try:
                                ht = int(input('Сколько шт.?  '))
                            except TypeError:
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
                                      f'денег осталось - {money}')
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
                                money += ot.warehouses[number].things[text_type].price + 3000 * ht
                                ot.warehouses[number].things[text_type].count -= ht
                                print(f'Было продано {ht} '
                                      f'{"принтеров" if tesh_type == 1 else "сканеров" if tesh_type == 2 else "ксераксов"} '
                                      f'денег стало - {money}')
                    except TypeError:
                        print('Command not found')
            elif user_command.isdigit() and int(user_command) == len(ot.warehouses) + 3:
                if input('Уничтожение склада продолжить (да/нет)?  ').lower() == "да":
                    ot.warehouses.pop(number)
    elif user_str.isdigit() and int(user_str) <= len(ot.warehouses) + 1:
        if input('Строительство склада стоит 5 млн. рублей продолжить (да/нет)?  ').lower() == "да":
            if money < 5000000:
                print('Недостаточно средств')
            else:
                ot.warehouses.append(Warehouse(input('В каком городе вы хотите построить склад?  ')))
                money -= 5000000
                print(f'У вас осталось {money} рублей')
