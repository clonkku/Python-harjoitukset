
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
        

class Kilpailu:
    def __init__(self, kilpailu_nimi, pituus, autojen_lista):
        self.kilpailu_nimi = kilpailu_nimi
        self.pituus = pituus
        self.autojen_lista = autojen_lista

    def tunti_kuluu(self):
        for auto in self.autojen_lista:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("rekisteritunnus \thuippunopeus \tnopeus \t        kuljettu_matka\n --------------------------------------------------------------------- ")
        for auto in self.autojen_lista:
            print(f"{auto.rekisteritunnus} \t\t\t{auto.huippunopeus} km/h \t{auto.nopeus} km/h \t{auto.kuljettu_matka} km")

    def kilpailu_ohi(self):
        for auto in self.autojen_lista:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


autot = []
for i in range(1, 11):
    huippunopeus1 = random.randint(100, 200)
    rekisteritunnus1 = f"ABC-{i}"
    auto = Auto(rekisteritunnus1, huippunopeus1)
    autot.append(auto)


kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while True:
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()
    if kilpailu.kilpailu_ohi():
        kilpailu.tulosta_tilanne()
        break






