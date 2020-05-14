import datetime


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def splitter(cls, date):
        return list(map(int, date.split('-')))

    @staticmethod
    def validation(date):
        data = date[2]
        d = datetime.date.today()
        date[2] = d.year if data > d.year else 2000 if data < 2000 else data
        data = date[1]
        if date[2] == d.year:
            date[1] = 1 if data < 1 else d.month if data > d.month else data
        else:
            date[1] = 1 if data < 1 else 12 if data > 12 else data
        data = date[0]
        if date[2] == d.year and date[1] == d.month:
            date[0] = 1 if data < 1 else d.day if data > d.day else data
        elif [1, 3, 5, 7, 8, 10, 12].count(date[1]):
            date[0] = 1 if data < 1 else 31 if data > 31 else data
        elif [4, 6, 9, 11].count(date[1]):
            date[0] = 1 if data < 1 else 30 if data > 30 else data
        else:
            date[0] = 1 if data < 1 else ((28 if date[2] % 4 else 29) if data > (28 if date[2] % 4 else 29) else data)
        return date


cl = Date(input('Введите дату в формате дд-мм-гггг: '))
result = cl.validation(cl.splitter(cl.date))
print(datetime.date(result[2], result[1], result[0]))
