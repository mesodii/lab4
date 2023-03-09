nom = input()
if int(len(nom)) % 2 != 0:
    print('Длина номера нечетная!')
else:
    sumpol1 = 0
    sumpol2 = 0
    pol = int(len(nom)/2)
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
