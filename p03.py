# 3. alkalom

'''import p03

szam = 10
while szam > 2:
    szam -= 1
    if szam == 4:
        continue
    if szam == 3:
        break
    print(szam)
else:
    print("Vége a ciklusnak")

while True:
    szam += 1
    print(szam)
    if szam == 30:
        break
'''

def szam_bekerese(legnagyobb_szam):
    szam = input("Kérek egy számot:")
    if szam.isdigit():
        szam = int(szam)
        if szam == 0:
            print("Nem ismerem a 0 számot")
        elif szam > legnagyobb_szam:
            print("Túl nagy számot kaptam")
        else:
            print("Most már tudok a számmal dolgozni")
    else:
        print("Nem számot adtál meg!")
    return szam

def szamologep():
    muvelet = input("Milyen műveletet akar végrehajtani (+,-,*,/):")
    egyik_szam = szam_bekerese(10)
    masik_szam = szam_bekerese(100)
    if muvelet == "+":
        eredmeny = egyik_szam + masik_szam
    elif muvelet == "-":
        eredmeny = egyik_szam - masik_szam
    elif muvelet == "*":
        eredmeny = egyik_szam * masik_szam
    else:
       eredmeny = egyik_szam / masik_szam
    print(f"Az eredmény: {egyik_szam} {muvelet} {masik_szam} = {eredmeny}")

def veletlenszam(max):
    import random
    szam = random.randint(0, max)
    return szam

def egesz_szam_bekerese():
    while True:
        szam = input("Kérek egy egész számot:")
        try:
            szam = int(szam)
            break
        except ValueError:
            print("Nem egész számot adott meg!")
    return szam


# A proram indítása
if __name__ == "__main__":
    print(egesz_szam_bekerese())

