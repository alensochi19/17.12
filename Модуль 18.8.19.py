allprice= 0
ticket = int(input('Введите количество приобретаемых билетов: '))
for i in range(ticket):
    i += 1
    visitor_age = int(input(f'Введите возраст {i} посетителя: '))
    if visitor_age < 18:
        print('Посетителям до 18 лет вход на конференцию бесплатный')
    elif 18 <= visitor_age < 25:
        allprice += 990
        print('Стоимость Вашего билета составляет: 990.0 руб.')
    else:
        allprice += 1390
        print('Стоимость Вашего билета составляет: 1 390.0 руб.')
if ticket > 3:
    allprice = allprice - (allprice*10/100)
    print()
    print(f'Сумма к оплате составляет: {allprice} руб. (с учетом 10%-ой скидки при регистрации более 3 посетителей)')
else:
    print()
    print(f'Сумма к оплате составляет: {allprice} руб.')
