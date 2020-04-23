def int_func(string):
    return string.capitalize()


string = input('Введите слово: ')
string = string.split()
for user_string in string:
    a_cods = []
    for i in user_string[1:]:
     a_cods.append(ord(i))
    user_string = int_func(user_string)
    user_string = user_string[:1]
    for i in a_cods:
        user_string = user_string + chr(i)
    print(user_string)