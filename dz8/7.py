class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма z1 и z2 равна\nz = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение z1 и z2 равно\nz = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


print('Ввод первого комплексного числа:')
z_1 = ComplexNumber(int(input('a: ')), int(input('b: ')))
print('Ввод второго комплексного числа:')
z_2 = ComplexNumber(int(input('a: ')), int(input('b: ')))
print(f'первое число\n{z_1}')
print(f'второе число\n{z_2}')
print(z_1 + z_2)
print(z_1 * z_2)