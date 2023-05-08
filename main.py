def proc1():
    ch = input()
    if int(ch) % 3 == 0:
        print('Число делится на 3')
    else:
        print('Число на 3 не делится')

def proc2():
    try:
        ch = input('Введите число: ')
        ans = 100 / int(ch)
    except ValueError:
        print('Введено не число!!')
    except ZeroDivisionError:
        print('Введите число отличное от 0!')
    else:
        print('Ответ:', ans)

def proc3():
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

def proc4():
    nom = input()
    if int(len(nom)) % 2 != 0:
        print('Длина номера нечетная!')
    else:
        sumpol1 = 0
        sumpol2 = 0
        pol = int(len(nom) / 2)
        pol1 = nom[:pol]
        pol2 = nom[-pol:]
        for i in range(len(pol1)):
            sumpol1 = sumpol1 + int(pol1[i])
        for l in range(len(pol2)):
            sumpol2 = sumpol2 + int(pol2[l])
        if sumpol1 == sumpol2:
            print('Этот билет счастливый!')
        else:
            print('Этот билет не счастливый:(')
proc1(), proc2(), proc3(), proc4()