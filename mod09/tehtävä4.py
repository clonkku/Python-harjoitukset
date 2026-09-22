import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tuntimaara):
        self.kuljettu_matka = self.kuljettu_matka + self.nopeus * tuntimaara
        




autot = []
kilpailu_ohi = False
for i in range(1, 11):
    huippunopeus1 = random.randint(100, 200)
    rekisteritunnus1 = f"ABC-{i}"
    auto = Auto(rekisteritunnus1, huippunopeus1)
    autot.append(auto)
while True:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kilpailu_ohi = True
            break
    if kilpailu_ohi:
        break

print("rekisteritunnus \thuippunopeus \tnopeus \t        kuljettu_matka ")
for auto in autot:
    print(f"{auto.rekisteritunnus} \t\t\t{auto.huippunopeus} km/h \t{auto.nopeus} km/h \t{auto.kuljettu_matka} km")


