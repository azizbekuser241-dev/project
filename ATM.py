kod  = int(input(('Kartangizni kodini kiriting kiriting : ')))
if kod == 2112:
    print('Tizimga kirildi!')
else:
    print("Parol xato!")

xizmat = input('Xizmat nomini kriting: ')
menyular1 = 'Naqd pul yechish'
menyu2 = 'Balansni tekshirish'
menyu3 = 'orqaga qytish'
menyu4 = 'parolni ozgartirish'
sorov = input('ushbu amaliyotda chekdan foydalanasizmi?: ')
balans = 1000000
summalar = 100000 , 200000 , 300000
boshqasumma = float(input('boshqa summa kiriting: '))
pin = int(input('sizning parolingiz: '))
if xizmat == menyular1:
    print(summalar)
    print(boshqasumma)
    print(sorov)
elif sorov == 'ha':
    print('muvafaqqiyatli amalga oshirildi!')
elif xizmat == menyu2:
    print(f'sizning balansingiz: {balans}')
elif xizmat == menyu3:
    print('orqaga qaytildi!')
elif xizmat == menyu4 :
    print(pin)
else: 
    print('bizda unaqa xizmat mavjud emas!')
    
