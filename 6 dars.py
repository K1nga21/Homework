mshaxs_1 = {'ism':'Lev Tolstoy',
           'tyil':1828,
           'vyil':1910,
           'tjoy':'Krapivenskoy'
           }

mshaxs_2 = {'ism':'Aleksandr Oushkun',
           'tyil':1799,
           'vyil':1837,
           'tjoy':'Sankt-Piterburg'
           }

mshaxs_3 = {'ism':'Gogol.N',
           'tyil':1821,
           'vyil':1852,
           'tjoy':"Yanovski"
           }

mshaxs_4 = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot"
           }

shaxslar = [mshaxs_1, mshaxs_2, mshaxs_3, mshaxs_4]

for shaxs in shaxslar:
    ism = shaxs['ism']
    tyil = shaxs['tyil']
    vyil = shaxs['vyil']
    tjoy = shaxs['tjoy']
    print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
          f"{vyil-tyil} yil umr ko'rgan.")


mshaxs_1 = {'ism':'Lev Tolstoy',
           'tyil':1828,
           'vyil':1910,
           'tjoy':'Krapivenskoy',
           'asarlar':["Детство","Война и мир","Анна Каренина"]
           }

mshaxs_2 = {'ism':'Aleksandr Pushkun',
           'tyil':1799,
           'vyil':1837,
           'tjoy':'Sankt-Piterburg',
           'asarlar':["Литературная энциклопедия","Энциклопедический словарь Брокгауза и Ефрона"]
           }

mshaxs_3 = {'ism':'Gogol.N',
           'tyil':1821,
           'vyil':1852,
           'tjoy':"Yanovski",
           'asarlar':["Ревизора","Мёртвых душ","Выбранных мест"]
           }

mshaxs_4 = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot",
           'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
           }

shaxslar = [mshaxs_1, mshaxs_2, mshaxs_3, mshaxs_4]

for shaxs in shaxslar:
    ism = shaxs['ism']
    asarlar = shaxs['asarlar']
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)

kinolar = {
    'otabek':['Onepunchman','Re-Zero','Onepiece'],
    'abdulaziz':['Uyda yolg\'iz','Mask','Interstellar'],
    'alisher':['Abdullajon','Temir odam','Tor'],
    'asad':['Jujusta Kaisen','John Wick']
    }

for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari va animelari:")
    for kino in kinolar:
        print(kino)

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm",
                   'prezident' : 'Shavkat Mirziyoyev'
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl",
                   'prezident' : 'Vladimir Putin'
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar",
                   'prezident' : 'Joe Biden'
    },
    "koreya":{'poytaxt':"seul",
                   'maydon':93210,
                   'aholi':28_000_000,
                   'pul birligi':"von",
                   'prezident' : 'Yoon Suk-yeol'
    }
    }

for davlat, info in davlatlar.items():
    if davlat.lower()=='aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}"
          f"\nPrezidenti: {info['prezident']}")
