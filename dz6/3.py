class Worker:
    def __init__(self,  name, surname, position, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def get_full_name(self):
        print(f'{self.surname} {self.name} - {self.position}')

    def get_total_income(self):
        print(f'Зарплата - {self._income["wage"] + self._income["bonus"]}')


p = Position(input('Имя: '), input('Фамилия: '), input('Должность: '), int(input('Зарплата: ')), int(input('Бонус: ')))
p.get_full_name()
p.get_total_income()