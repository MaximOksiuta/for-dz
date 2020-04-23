def info(name, surname, year, city, email, phone):
    print(
        f'{name} {surname} родился в {year} году, проживает в городе {city}, email - {email}, номер телефона - {phone}')


info(name=input('Ваше имя: '), surname=input('Ваша фамилия: '), year=input('В каком году вы родились? '),
     city=input('В каком городе живёте? '), email=input('Ваш Email: '), phone=input('Ваш номер телефона: '))