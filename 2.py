try:
    ch = input('Введите число: ')
    ans = 100 / int(ch)
except ValueError:
    print('Введено не число!!')
except ZeroDivisionError:
    print('Введите число отличное от 0!')
else:
    print('Ответ:', ans)