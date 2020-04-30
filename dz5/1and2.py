while True:
    u_string = input('Для выхода нажмите Enter\nВведите строку которую хотите записать в файл: ')
    if u_string == '':
        break
    try:
        with open("new_f.txt", 'a', encoding='utf-8') as f_obj:
            f_obj.write(f'{u_string}\n')
    except IOError:
        print('IOError')
itog_words = 0
with open("new_f.txt", 'r', encoding='utf-8') as f_obj:
    strings = f_obj.readlines()
    i = 1
    for string in strings:
        words = len(string.split())
        print(f'{i} строка - {string} - {words} слов')
        itog_words += words
        i += 1
print(f'Всего {i-1} строк и {itog_words} слов')
