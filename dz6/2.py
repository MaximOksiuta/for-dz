class Road:
    def __init__(self, length, width, m, thickness):
        self._m = m
        self._thickness = thickness
        self._lenght = length
        self._width = width

    def massa(self):
        return self._lenght*self._width*self._m*self._thickness


print("Укажите данные в 'м' и 'кг', толщину в 'см'")
r = road(int(input('Длина: ')), int(input('Ширина: ')), int(input('Масса: ')), float(input('Толщина: ')))
print(f'{r.massa()} кг')