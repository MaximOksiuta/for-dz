with open("text_3.txt", 'r', encoding='utf-8') as f:
    content = f.readlines()
    av_salary = 0
    for i in content:
        string = i.split()
        try:
            salary = float(string[1])
        except ValueError:
            print('Зарплата это число!')
        try:
            if salary < 20000.0:
                print(string)
            av_salary += salary
        except NameError:
            print()
try:
    av_salary /= len(content)
except ZeroDivisionError:
    print('В файле должно быть хоть что-то')
print(f'Средняя зарплата сотрудников - {av_salary}')