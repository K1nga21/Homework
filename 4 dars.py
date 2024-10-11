son = float(input("Juft son kiriting: "))
if son%2:
    print('Bu son juft emas.')
else:
    print("Rahmat!")


yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0;
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
    else:
        print(f"Uzur 2 dan 10 gacha bolgan sonlarni kiriting")

otam = {'ismi':'azamat', 'tyil':1977,'viloyat':'xorazm'}
onam = {'ismi':'iroda', 'tyil':1979,'viloyat':'xorazm'}
t_yil = onam['tyil']
vil_1 = onam['viloyat']
tyil = otam['tyil']
vil = otam['viloyat']
print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")
print(f"Onamning ismi {onam['ismi'].title()}, {t_yil}-yilda, {vil_1.title()} viloyatida tug'ilgan")

taomlar = {
    'azamat':'baliq',
    'iroda':'osh',
    'otabek':"lag'mon",
    'munisa':"fast food",
    'aziznek':"shashlik"
    }

taom = taomlar['azamat']
taom = taomlar['iroda']
taom = taomlar['otabek']
print(f"Azamatning sevimli taomi {taom}\
    Irodaning sevimli taomi {taom}\
    Otabekning sevimli taomi {taom}")


python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat",
    'def' : "Bir indexni o'chirb tashlaydi",
    'remove' : "O'rnini almashtiradi"
}
print(python_izohli_lugati['def'])

lugat = {
    'book':"kitob",
    'game':"oyin",
    'string':"matn",
    'delete':"ochirish",
    'copmuter':"komyuter",
    'online' : "tarmoqda",
    'walk' : "yurish"
}
sozlar = input("So'z kiriting:").lower()
tarjima = lugat.get(sozlar)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{sozlar.title()} so'zi {tarjima} deb tarjima qilinadi")
