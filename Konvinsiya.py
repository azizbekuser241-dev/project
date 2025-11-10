print('Konversiya xizmariga xush kelibsiz!(NBU)')
while True:
    print("Bizda bor valyutalar(UZS): ")
    valyutalar = {'1)Dollar(USD)' : 12050 , 
              '2)Rubl(Rub)' : 160,
              '3)Yaponya tangasi(JPY)' : 85 , 
              "4)kazakstan(KZT)" : 23,
              '5) chiqish' : 0}
    for valyuta in valyutalar:
        print(valyuta)
    sorov1 = int(input('Qaysi valyutani olmoqchisiz(1-5), Tanlang: '))
    if sorov1 == 1:
        dollar = float(input('Qancha dollar olmoqchisiz: '))
        print(dollar)
        naqd = dollar * 12050
        print(f'siz {dollar} dollar uchun {naqd} som pul tolashingiz kerak!')
    elif sorov1 == 2:
        Rubl = float(input('Qancha rubl olmoqchisiz: '))
        print(Rubl)
        naqd1 = Rubl * 160
        print(f'siz {Rubl} rubl uchun {naqd1} som tolashingiz kerak!')
    elif sorov1 ==  3:
        JPY = float(input('Qancha (JPY) olmoqchisiz: '))
        print(JPY)
        naqd2 = JPY * 85
        print(f'Siz {JPY} JPY uchun {naqd2} som pul tolashingiz kerak!')
    elif sorov1 == 4:
        KZT = float(input('Qancha KZT olmoqchisiz: '))
        print(KZT)
        naqd3 = KZT * 23
        print(f'Siz {KZT} KZT uchun {naqd3} som pul tolashingiz kerak!')
    elif sorov1 == 5:
        print('Bizni tanlaganingiz uchun rahmat!')
        break
    else:
        print('Bu raqamda servis xizmati mavjud emas!')
        break