import p03
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

