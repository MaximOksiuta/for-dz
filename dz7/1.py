class Matrix:
    """перегрузка конструктора"""
    def __init__(self, matrix):
        self.matrix = matrix

    """перегрузка __str__"""
    def __str__(self):
        self.result = ''   # очистка итоговой строки
        self.matrix = self.checker(self.matrix)
        """формирование матрицы"""
        for i in self.matrix:
            for n in i:
                self.result += f'{n}  '
            self.result += '\n'
        return self.result  # возвращаем готовую матрицу

    """метод для проверки матрицы и устронения не соответствий"""
    def checker(self, mat, m=0, ls=1):
        """создание списка длин строк (если нужно)"""
        if ls == 1:
            ls = [len(i) for i in mat]
        """нахождение максимального количества чисел в строке (если нужно)"""
        if m == 0:
            m = max(ls)
        """дополнение строк '0' (если нужно)"""
        c = 0
        for i in ls:
            if i != m:
                for n in range(0, m - i):
                    mat[c].append(0)
            c += 1
        return mat   # возвращаем корректную матрицу

    """перегрузка __add__"""
    def __add__(self, other):
        s_len = len(self.matrix)    # нахождение количества строк 1 матрицы
        o_len = len(other.matrix)   # нахождение количества строк 2 матрицы
        """проверка и исправление различий в количестве строк"""
        if s_len < o_len:
            for i in range(0, o_len - s_len):
                self.matrix.append([])
        elif s_len > o_len:
            for i in range(0, s_len - o_len):
                other.matrix.append([])
        ls = [len(i) for i in self.matrix]     # создание списка длин строк 1 матрицы
        ls2 = [len(i) for i in other.matrix]   # создание списка длин строк 2 матрицы
        lm = ls + ls2   # соединение двух списков для нахождения максимального количества чисел в строке
        m = max(lm)
        self.matrix = self.checker(self.matrix, m, ls)  # обращаемся к функции checker для проверки и исправления строк
        other.matrix = other.checker(other.matrix, m, ls2)
        self.result = ''  # очистка итоговой строки
        """формирование матриц и их сложение"""
        for i in range(0, len(self.matrix)):
            for n in range(0, len(self.matrix[i])):
                self.result += f'{self.matrix[i][n] + other.matrix[i][n]}  '
            self.result += '\n'
        return self.result  # возвращаем готовую матрицу


matrix = [[1, 2], [3, 4], [5, 6]]
matrix1 = [[7, 8], [9, 10], [11, 12, 13], []]
M = Matrix(matrix)
M1 = Matrix(matrix1)
print(M)
print(M1)
print(M+M1)
