savol = "Sevgan kitobingizni kiriting"

while True:
    kitob = input(savol)
    if kitob == 'exit':
        break
print('Rahmat!')

savol = "Yoshingizni kiriting: "

while True:
    value = input(savol)
    if value == 'exit' or value == 'quit':
        break
    yosh = int(value)

    if yosh < 7:
        price = 2000
    elif 7 <= yosh < 18:
        price = 3000
    elif 18 <= yosh < 65:
        price = 10000
    else:
        price = 0

    if price == 0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {price} so'm")


savat =[]
while True:
    mahsulot = input("Savatga mahsulot qo'shing:")
    savat.append(mahsulot)
    answer = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
    if answer != 'ha':
        break

buyurtmalar = ['olma','anor','uzum','banan']
mahsulotlar = {'olma':26580,
               'shaftoli':25000,
               'qovun':18000,
               'banan':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
