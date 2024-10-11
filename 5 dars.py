dictonary = {
    'book' : 'kitob',
    'massa' : 'massa',
    'bye' : 'xayr',
    'programm' : 'programma',
    'app' : 'ilova',
    'play' : 'oynamoq',
    'leave' : 'ketmoq',
    'welcome' : 'xush kelibsiz',
    'name' : 'ism',
    'surname' : 'familiya'
}

for key, value in sorted(dictonary.items()):
    print(f"{key.title()} - {value}")


davlatlar = {
    'usa' : 'washington',
    'uzbekiston' : 'tashkent',
    'yaponiya' : 'tokyo',
    'rossiya' : 'moskva',
    'qozohiston' : 'astana',
    'italiya' : 'rim',
    'singapur' : 'singapur',
    'baa' : 'abu-dabi',
    'braziliya' : 'rio',
    'tojikiston' : 'dushanbe'
}
print("Dunyo davlatlari")
for davlat in sorted(davlatlar):
  print(davlat.upper)
print('\nDavlatlarning poytaxtlari')
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())
country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = davlatlar.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")


menu = {
        'osh':1700,
        "lag'mon":25000,
        'non':3000,
        'choy':2000,
        'shashlik':10000,
        'gamurg' : 13000,
        'somsa':10000,
        'tabaka':35000,
        'fetchi' : 10000,
        'hot-dog' : 7000,
        'turk kabob' : 21000
        }

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for a in range(3):
    buyurtmalar.append(input(f"{a+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")
