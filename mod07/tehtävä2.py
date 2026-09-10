import random
def noppaluku(tahkot):
    noppa = random.randint(1, tahkot)
    return noppa


maksimi = int(input("Mikä on nopan maksimisilmäluku?\n"))
noppa = noppaluku(maksimi)
while noppa != maksimi:
    print(noppa)
    noppa = noppaluku(maksimi)

print(noppa)