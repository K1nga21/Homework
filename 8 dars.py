def tyil_hisobla(ism, yosh):
    """Foydalanuvchi tugilgan yilini hisoblovchi funksiya"""
    print(f"{ism.title()} {2024-yosh}-yilda tug'ilgan")


tyil_hisobla("otabek", 23)


def kv_kub(a):
    print(f"{a} ning kvadrati {a**2} va kubi {a**3}")


kv_kub(87)


def son(x, y):
    if x > y:
        print(f"{x}>{y}")
    elif x < y:
        print(f"{y}>{x}")
    else:
        print(f"Sonlar teng {x}={y}")


son(1318, 6465)
son(-89, 168)
son(298, 298)
