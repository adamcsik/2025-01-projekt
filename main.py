try:
    eredmeny = 10 / ertek
except ZeroDivisionError:
    print("HIBA: Nullával való osztás")
except NameError:
    print("HIBA: névhiba")
else:
    print(eredmeny)

