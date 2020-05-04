class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        is_police = is_police

    def go(self):
        print('Машина едет')

    def turn(self, direction):
        print(f'Машина поворачивает {direction}')

    def stop(self):
        print('Машина останавливается')

    def show_speed(self):
        print(f'Текущая скорость машины - {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')


class PoliceCar(Car):
    pass


car_type = input('Введите тип машины (Town, Sport, Work, Police): ')
if car_type == 'Town':
    car = TownCar(int(input('Скорость: ')), input('Цвет: '), input('Модель: '), False)
elif car_type == 'Sport':
    car = SportCar(int(input('Скорость: ')), input('Цвет: '), input('Модель: '), False)
elif car_type == 'Work':
    car = TownCar(int(input('Скорость: ')), input('Цвет: '), input('Модель: '), False)
elif car_type == 'Police':
    car = TownCar(int(input('Скорость: ')), input('Цвет: '), input('Модель: '), True)
else:
    print('Введите тип из списка!')
car.show_speed()
while True:
    move = input('Введите действие (Go, stop, turn): ')
    if move == 'Go':
        car.go()
    elif move == 'Stop':
        car.stop()
    elif move == 'Turn':
        car.turn(input('Введите направление поворота: '))
    else:
        break
