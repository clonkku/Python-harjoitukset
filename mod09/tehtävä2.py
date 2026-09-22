"""Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää."""
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka
    def kiihdyta(self, nopeuden_muutos):
        self.nopeuden_muutos = nopeuden_muutos
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus


auto1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus on {auto1.rekisteritunnus} ja sen huippunopeus on {auto1.huippunopeus} km/h, auto kulkee tällä hetkellä {auto1.nopeus} km/h ja sillä on ajettu {auto1.kuljettu_matka} km")
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"auto kulkee nyt {auto1.nopeus} km/h")
auto1.kiihdyta(-200)
print(f"auto kulkee nyt {auto1.nopeus} km/h")
