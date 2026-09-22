"""Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km."""
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
        



auto1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus on {auto1.rekisteritunnus} ja sen huippunopeus on {auto1.huippunopeus} km/h, auto kulkee tällä hetkellä {auto1.nopeus} km/h ja sillä on ajettu {auto1.kuljettu_matka} km")
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"auto kulkee nyt {auto1.nopeus} km/h")
auto1.kulje(1.5)
print(f"auto on kulkenut {auto1.kuljettu_matka} km")
auto1.kiihdyta(-200)
print(f"auto kulkee nyt {auto1.nopeus} km/h")
