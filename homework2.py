ad = input('Ad: ')
soyad = input('Soyad: ')
yaş = int(input('Yaş: '))
dogum = int(input('Doğum Yılı: '))
udlist = [f'{ad}',f'{soyad}',f'{yaş}',f'{dogum}']
print(udlist)
if yaş < 0:
    print("Geçersiz değer")
else:
    if yaş < 18:
        print("Sokağa çıkmanız tehlikeli, lütfen çıkmayın!")
    else:
        18 < yaş
        print("Sokağa çıkabilirsiniz.")