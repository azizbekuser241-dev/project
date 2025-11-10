print('Assalomu alaykum ,Avtoservisga xush kelibsiz!')
print("Bizda bor xizmatlar: ")
print('1) Polirovka')
print("2) Moyka")
print("3) Moy almashtirish")
print("4) Zapchast almashtirish")
print("5) chiqish")
xizmat = int(input('xizmat nomini kiriting: '))
if xizmat == 1:
    print('Polirovka narxi 200000')
    sorov3 = input('polirovkaga rozimisiz?(ha/yoq) ')
    if sorov3 == 'ha':
        print('ok')
    
elif xizmat == 2:
    print("1) Vosk")
    print("2) Pena")
    print("3) Voda")
    print("4) Aktivnaya ximiya")
    moyka = int(input("Tanlang(1-4): "))
    if  moyka == 1:
        print('started (vosk) 15000 sums')

    if moyka == 2:
        print('started (pena) 1l = 10000 sums')
    if moyka == 3:
        print('started (voda) 1l = 5000 sums')
    if moyka == 4:
        print("started (aktivnaya ximiya) 20000 sums")
elif xizmat == 3:
    print('Moy almashtirishga konglingizdan chiqqanini bering!')
    sorov4 = input('Tayyormisiz(ha/yoq) ')
    if sorov4 == 'ha':
        print('ok')
elif xizmat == 4:
    print('Qanday zapchast almashtirmoqchisiz?')
    print('1) bamper')
    print('2) kuzuf')
    print('3) paralar')
    zapchast = int(input('kiriting: '))
    if zapchast == 1:
        print('600000 sums (bamper)')
    if zapchast == 2:
        print('1500$ (kuzuf)')
        sorov = input('Almashtirasizmi:(ha/yoq) ')
    if sorov == 'ha':
        print('Ok')
    if zapchast == 3:
        print('200$ (paralar)')
    
        sorov1 = input('Almashtirasizmi:(ha/yoq) ')
    if sorov1 == 'ha':
        print("oook!")
elif xizmat == 5:
    print("Bizni tanlaganingiz uchu raxmat! . Bye!")
else:
    print('Bizda bu nomerda servis yoq!')
