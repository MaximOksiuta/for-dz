from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name: str, size: int, height: int):
        self.name = name
        self.size = size
        self.height = height

    @abstractmethod
    def textil_sum(self):
        pass


# класс пальто
class Coat(Clothes):
    def __init__(self, name: str, size: int, height=0):
        super(Coat, self).__init__(name, size, height)

    def textil_sum(self):
        return (self.size / 6.5 + 0.5)


# класс костюм
class Suit(Clothes):
    def __init__(self, name: str, height: int, size=0):
        super(Suit, self).__init__(name, size, height)

    def textil_sum(self):
        return (self.size * 2 + 0.3)


while True:
    # запрашиваем данные у пользователя
    string = input('Введите тип одежды (coat или suit): ')
    # обрабатываем и выводим результат
    if string == 'coat':
        coat = Coat('coat', int(input('Введите размер: ')))
        print(coat.textil_sum())
    elif string == 'suit':
        suit = Suit('suit', int(input('Введите рост: ')))
        print(suit.textil_sum())
    else:
        print('Тип одежды может быть только coat или suit!')