print('Assalomu alaykum')
print('Agrobank kredit markaziga xush kelibsiz!')
mablag = 100_000_000
print(f'Bizning bankimizda {mablag} som pul bor!')
sizga_kerak_kredit = float(input('olmoqchi bolgan kreditingizni qiymatini kiriting: '))
if sizga_kerak_kredit <= mablag:
    foiz = float(input('Foizni ozimiz tanlaymiz (hozirgi yil boyicha):  '))
    yillik_foiz = sizga_kerak_kredit + (sizga_kerak_kredit * foiz)
    print(f'siz {sizga_kerak_kredit} somni bir yilda {yillik_foiz} som qilib qaytarishingiz kerak!')
    oyiga = sizga_kerak_kredit / 12
    print(f'siz {sizga_kerak_kredit} somni 1 oydan qaytarmoqchi bolsangiz , oyiga {oyiga} som tolashingiz lozim!')
    oy_kuni = float(input('Tolov oyini nechanchi kuni: '))
    if oy_kuni > 30 :
        kechikish = oyiga + (oyiga * 0.1)
        print(f'Agar siz 1 oydan kechikib qaytarmoqchi bolsangiz {kechikish} som qilib qaytarishingizga togri keladi!')
        aksiya = sizga_kerak_kredit
    oyiga_aksiya = sizga_kerak_kredit / 12
    print(f"Agar siz 1-noyabrgacha  aksiyada qatnashsangiz {sizga_kerak_kredit} somni  1 yilda ozini qaytarish imkoniyatiga egasiz va oyiga kechiksangiz ham {oyiga_aksiya} somni ozini qaytarish imkoniyatiga egasiz!")
    print('Bu aksiya faqat 2025-yil uchun amal qialdi!')
    print('Bizda hozirda shu amaliyotlar bor!')
    print('Bizni tanlaganingiz uchun raxmat!')
else:
    print(f'Afsuski bizda hozircha {mablag} somdan kop pul yoq!')