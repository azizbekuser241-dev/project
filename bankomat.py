balans = 1_000_000
parol = 1234

parol2 = int(input("Parolni kiriting: "))
uz = "1) O'zbek tili!"
rus = "2) Русcкий язик!"
eng = "3) English language!"
print(uz)
print(rus)
print(eng)
til = (input("Til tanlang! "))

if til == "1":
    while True:
        if parol == parol2:
            print("\nTizimga kirildi")

            print("Ammalardan birortasni kiriting")
            print("1) Balansni tekshrish")
            print("2) Naqt pul yechish ")
            print("3) Pul qo'shish")    
            print("4) Mobil aloqalarga to'lov")
            print("5) Chqish")
            amallarkirdi = int(input("Kiriting: "))

            if amallarkirdi == 1:
                print(balans)

            elif amallarkirdi == 2:
                balansdan_olish = float(input("Yechib olmoqchi bo'lgan summani kiring: "))

                balansdan_olish = float(balansdan_olish)
                foiz = balansdan_olish * 0.01

                balans = (balans - balansdan_olish) - foiz
                print(f"Balansingizda {balans} so'm bor")
            elif amallarkirdi == 3:

                balansga_pul_qoshish = float(input("Qo'shmoqchi bo'lgan summani kriting: "))

                foiz2 = balansga_pul_qoshish * 0.01
                balans = (balans + balansga_pul_qoshish)- foiz2
                print(f"Balansingizda {balans} so'm bor")
            elif amallarkirdi == 4:
                print("1) Uzmobile\n2) Beeline\n3) Uccel\n4) UMS\n5) Humans\n6) UzTelecom")
            
                qaysi = int(input("Qaysi kompanyaga pul o'tkazmoqchisiz? "))
                if qaysi == 1:
                    print("Siz Uzmobilega pul o'tkazmoqchisiz! Kod: 99/95/77")
                    telefon_raqam = int(input("Raqamni kirting: +998 "))
                    tolov = float(input("To'lov summasini kiritng: "))
                    print(f"Hisobingiz {tolov} ga to'ldirildi!\nKartangizda: {balans - tolov} so'm bor")
                elif qaysi == 2:
                    print("Siz Beelinega pul o'tkazmoqchisiz! Kod: 91/90")
                    telefon_raqam = int(input("Raqamni kirting: +998 "))
                    tolov = float(input("To'lov summasini kiritng: "))
                    print(f"Hisobingiz {tolov} ga to'ldirildi!\nKartangizda: {balans - tolov} so'm bor")
                elif qaysi == 3:
                    print("Siz Uccelga pul o'tkazmoqchisiz! Kod: 93/94/50")
                    telefon_raqam = int(input("Raqamni kirting: +998 "))
                    tolov = float(input("To'lov summasini kiritng: "))
                    print(f"Hisobingiz {tolov} ga to'ldirildi!\nKartangizda: {balans - tolov} so'm bor")
                elif qaysi == 4:
                    print("Siz UMSga pul o'tkazmoqchisiz! Kod: 88/33/97/55")
                    telefon_raqam = int(input("Raqamni kirting: +998 "))
                    tolov = float(input("To'lov summasini kiritng: "))
                    print(f"Hisobingiz {tolov} ga to'ldirildi!\nKartangizda: {balans - tolov} so'm bor")
                elif qaysi == 5:
                    print("Siz Humansga pul o'tkazmoqchisiz! Kod: 33")
                    telefon_raqam = int(input("Raqamni kirting: +998 "))
                    tolov = float(input("To'lov summasini kiritng: "))
                    print(f"Hisobingiz {tolov} ga to'ldirildi!\nKartangizda: {balans - tolov} so'm bor")
                elif qaysi == 6:
                    print("Siz Uztelecom pul o'tkazmoqchisiz! Kod: Wifi")
                    telefon_raqam = int(input("Raqamni kirting: "))
                    tolov = float(input("To'lov summasini kiritng: "))
                    print(f"Hisobingiz {tolov} ga to'ldirildi!\nKartangizda: {balans - tolov} so'm bor")

            elif amallarkirdi == 5:
                print("Bizni tanlagangiz uchun rahmat")
                break
            else:
                print("Parol xato/n")
elif til == "2":
    while True:
        if parol == parol2:
            print("\nВход в систему выполнен")
            print("Выберите одно из действий:")
            print("1) Проверить баланс")
            print("2) Снять наличные")
            print("3) Пополнить счёт")    
            print("4) Оплата мобильной связи")
            print("5) Выход")
            amallarkirdi = int(input("Введите номер действия: "))

            if amallarkirdi == 1:
                print(balans)

            elif amallarkirdi == 2:
                balansdan_olish = float(input("Введите сумму, которую хотите снять: "))

                balansdan_olish = float(balansdan_olish)
                foiz = balansdan_olish * 0.01

                balans = (balans - balansdan_olish) - foiz
                print(f"На вашем счёте осталось {balans} сумов")

            elif amallarkirdi == 3:
                balansga_pul_qoshish = float(input("Введите сумму, которую хотите внести: "))

                foiz2 = balansga_pul_qoshish * 0.01
                balans = (balans + balansga_pul_qoshish) - foiz2
                print(f"На вашем счёте {balans} сумов")

            elif amallarkirdi == 4:
                print("1) Uzmobile\n2) Beeline\n3) Ucell\n4) UMS\n5) Humans\n6) UzTelecom")
                
                qaysi = int(input("В какую компанию хотите перевести деньги? "))
                if qaysi == 1:
                    print("Вы выбрали Uzmobile! Код: 99/95/77")
                    telefon_raqam = int(input("Введите номер телефона: +998 "))
                    tolov = float(input("Введите сумму платежа: "))
                    print(f"Ваш счёт пополнен на {tolov} сумов!\nНа карте осталось: {balans - tolov} сумов")
                elif qaysi == 2:
                    print("Вы выбрали Beeline! Код: 91/90")
                    telefon_raqam = int(input("Введите номер телефона: +998 "))
                    tolov = float(input("Введите сумму платежа: "))
                    print(f"Ваш счёт пополнен на {tolov} сумов!\nНа карте осталось: {balans - tolov} сумов")
                elif qaysi == 3:
                    print("Вы выбрали Ucell! Код: 93/94/50")
                    telefon_raqam = int(input("Введите номер телефона: +998 "))
                    tolov = float(input("Введите сумму платежа: "))
                    print(f"Ваш счёт пополнен на {tolov} сумов!\nНа карте осталось: {balans - tolov} сумов")
                elif qaysi == 4:
                    print("Вы выбрали UMS! Код: 88/33/97/55")
                    telefon_raqam = int(input("Введите номер телефона: +998 "))
                    tolov = float(input("Введите сумму платежа: "))
                    print(f"Ваш счёт пополнен на {tolov} сумов!\nНа карте осталось: {balans - tolov} сумов")
                elif qaysi == 5:
                    print("Вы выбрали Humans! Код: 33")
                    telefon_raqam = int(input("Введите номер телефона: +998 "))
                    tolov = float(input("Введите сумму платежа: "))
                    print(f"Ваш счёт пополнен на {tolov} сумов!\nНа карте осталось: {balans - tolov} сумов")
                elif qaysi == 6:
                    print("Вы выбрали UzTelecom! Код: Wi-Fi")
                    telefon_raqam = int(input("Введите номер: "))
                    tolov = float(input("Введите сумму платежа: "))
                    print(f"Ваш счёт пополнен на {tolov} сумов!\nНа карте осталось: {balans - tolov} сумов")

            elif amallarkirdi == 5:
                print("Спасибо, что выбрали нас!")
                break
            else:
                print("Неверный пароль\n")
elif til == "3":
    while True:
        if parol == parol2:
            print("\nLogged into the system")

            print("Choose one of the following options:")
            print("1) Check balance")
            print("2) Withdraw cash")
            print("3) Deposit money")    
            print("4) Pay for mobile services")
            print("5) Exit")
            amallarkirdi = int(input("Enter your choice: "))

            if amallarkirdi == 1:
                print(balans)
            elif amallarkirdi == 2:
                balansdan_olish = float(input("Enter the amount you want to withdraw: "))

                balansdan_olish = float(balansdan_olish)
                foiz = balansdan_olish * 0.01

                balans = (balans - balansdan_olish) - foiz
                print(f"You have {balans} sums left in your account")

            elif amallarkirdi == 3:
                balansga_pul_qoshish = float(input("Enter the amount you want to deposit: "))

                foiz2 = balansga_pul_qoshish * 0.01
                balans = (balans + balansga_pul_qoshish) - foiz2
                print(f"Your balance is {balans} sums")

            elif amallarkirdi == 4:
                print("1) Uzmobile\n2) Beeline\n3) Ucell\n4) UMS\n5) Humans\n6) UzTelecom")
                
                qaysi = int(input("Which company do you want to send money to? "))
                if qaysi == 1:
                    print("You chose Uzmobile! Code: 99/95/77")
                    telefon_raqam = int(input("Enter phone number: +998 "))
                    tolov = float(input("Enter payment amount: "))
                    print(f"The number has been topped up by {tolov} sums!\nYour remaining balance: {balans - tolov} sums")
                elif qaysi == 2:
                    print("You chose Beeline! Code: 91/90")
                    telefon_raqam = int(input("Enter phone number: +998 "))
                    tolov = float(input("Enter payment amount: "))
                    print(f"The number has been topped up by {tolov} sums!\nYour remaining balance: {balans - tolov} sums")
                elif qaysi == 3:
                    print("You chose Ucell! Code: 93/94/50")
                    telefon_raqam = int(input("Enter phone number: +998 "))
                    tolov = float(input("Enter payment amount: "))
                    print(f"The number has been topped up by {tolov} sums!\nYour remaining balance: {balans - tolov} sums")
                elif qaysi == 4:
                    print("You chose UMS! Code: 88/33/97/55")
                    telefon_raqam = int(input("Enter phone number: +998 "))
                    tolov = float(input("Enter payment amount: "))
                    print(f"The number has been topped up by {tolov} sums!\nYour remaining balance: {balans - tolov} sums")
                elif qaysi == 5:
                    print("You chose Humans! Code: 33")
                    telefon_raqam = int(input("Enter phone number: +998 "))
                    tolov = float(input("Enter payment amount: "))
                    print(f"The number has been topped up by {tolov} sums!\nYour remaining balance: {balans - tolov} sums")
                elif qaysi == 6:
                    print("You chose UzTelecom! Code: Wi-Fi")
                    telefon_raqam = int(input("Enter number: "))
                    tolov = float(input("Enter payment amount: "))
                    print(f"The number has been topped up by {tolov} sums!\nYour remaining balance: {balans - tolov} sums")

            elif amallarkirdi == 5:
                print("Thank you for choosing us!")
                break
            else:
                print("Incorrect password\n")

else:
    print("Bunday raqam bilan til mavjud emas")
