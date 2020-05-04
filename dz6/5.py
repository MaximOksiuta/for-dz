class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


w_type = input('Чем рисовать? (Pen, Pencil, Handle): ')
if w_type =='Pen':
    drawer = Pen(input('Что писать? '))
elif w_type == 'Pencil':
    drawer = Pencil(input('Что писать? '))
elif w_type == 'Handle':
    drawer = Handle(input('Что писать? '))
else:
    drawer = Stationery(input('Что писать? '))
drawer.draw()