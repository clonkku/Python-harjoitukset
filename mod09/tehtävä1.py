class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

auto1 = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus on {auto1.rekisteritunnus} ja sen huippunopeus on {auto1.huippunopeus} km/h, auto kulkee tällä hetkellä {auto1.nopeus} km/h ja sillä on ajettu {auto1.kuljettu_matka} km")
