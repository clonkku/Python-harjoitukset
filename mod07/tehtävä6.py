import math
def pizza(halkaisija, hinta):
    sade = halkaisija / 2
    pintaala = math.pi * sade ** 2
    yksikkohinta = hinta / pintaala * 10000
    return yksikkohinta

halkaisija1 = float(input("Kerro ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Kerro ensimmäisen pizzan hinta: "))
halkaisija2 = float(input("Kerro toisen pizzan halkaisija: "))
hinta2 = float(input("Kerro toisen pizzan hinta: "))

yksikko1 = pizza(halkaisija1, hinta1)
yksikko2 = pizza(halkaisija2, hinta2)

if yksikko1 < yksikko2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikko1 > yksikko2:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat saman arvoisia neliömetriltä")