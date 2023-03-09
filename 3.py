try:
    data = input('Введите дату в нужном формате: ')
    data = data.split('.')
except ValueError:
    print('Введите дату числами!')
else:
    if int(data[0]) * int(data[1]) == int(data[2][-2:]):
        print('Это магическое число｡*:☆')
    else:
        print('Это не магическое число:(')