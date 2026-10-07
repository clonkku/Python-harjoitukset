import time
import random

pelaajannimi = input("Mikä sinun nimesi on?\n")
pelaajanikä = input(f"Hauska tavata {pelaajannimi}! Mikä sinun ikäsi on?\n")


class Pelaaja:
    def __init__(self, nimi, esinelista, sijainti):
        self.nimi = nimi
        self.esinelista = esinelista
        self.sijainti = sijainti

    def liiku(self, seuraava_huone):
        self.sijainti = seuraava_huone

    def keraa_esine(self):
        if self.sijainti.mahd_esine is not None:
            self.esinelista.append(self.sijainti.mahd_esine)
            print(f"Keräsit esineen: {self.sijainti.mahd_esine.nimi}")
            self.sijainti.mahd_esine = None
        else:
            print("Tässä huoneessa ei ole esinettä.")


class Huone:
    def __init__(self, nimi, mahd_esineet):
        self.nimi = nimi
        self.mahd_esine = random.choice(mahd_esineet)


class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino


def inventaario():
    while True:
        print("=== Inventaario ===")

        if len(pelaaja.esinelista) == 0:
            print("Inventaario on tyhjä!")
        else:
            for esine in pelaaja.esinelista:
                print(f"{esine.nimi}, paino: {esine.paino} g")

        valinta = input("1. Takaisin päävalikkoon\nValitse: ")

        if valinta == "1":
            break


def lepaa():
    print("Menit nukkumaan...")
    uniaika = 5

    while uniaika != 0:
        time.sleep(1)
        print("zZzZzZzZ...")
        uniaika = uniaika - 1

    if random.randint(1, 5) == 1:
        print("Heräsit väsyneenä >:(")
    else:
        print("Heräsit virkeänä! :)")

    time.sleep(3)


# Luodaan esineet
mahd_esineet = []

mahd_esineet.append(Esine("muovipussi", 25))
mahd_esineet.append(Esine("tölkki", 50))
mahd_esineet.append(Esine("Putkipommi"))



# Luodaan huoneet
vessa = Huone("Vessa", mahd_esineet)
keittio = Huone("Keittiö", mahd_esineet)
olohuone = Huone("Olohuone", mahd_esineet)
kellari = Huone("Kellari", mahd_esineet)
parveke = Huone ("Parveke", mahd_esineet)
makuuhuone = Huone("Makuuhuone", mahd_esineet)

# Luodaan pelaaja
inventaario1 = []

pelaaja = Pelaaja(pelaajannimi, inventaario1, keittio)


while True:

    print("\n=== Päävalikko ===")
    print(f"Olet huoneessa: {pelaaja.sijainti.nimi}")
    if pelaaja.sijainti.mahd_esine is not None:
        print(f"Huoneessa on esine: {pelaaja.sijainti.mahd_esine.nimi}")
    else:
        print("Huoneessa ei ole kerättävää esinettä")
    print("1. Vessa")
    print("2. Keittiö")
    print("3. Olohuone")
    print("4. Kerää esine")
    print("5. Näytä inventaario")
    print("6. Nuku")
    print("7. Lopeta peli")

    valinta = int(input("Valitse: "))

    if valinta == 1:
        pelaaja.liiku(vessa)
    if valinta == 2:
        pelaaja.liiku(keittio)
    if valinta == 3:
        pelaaja.liiku(olohuone)
    if valinta == 4:
        pelaaja.liiku
        if pelaaja.sijainti == keittio:
            pelaaja.liiku(keittio)
        elif pelaaja.sijainti == olohuone:
            pelaaja.liiku(vessa)

        elif pelaaja.sijainti == vessa:
            pelaaja.liiku(keittio)

        print(f"Siirryit huoneeseen: {pelaaja.sijainti.nimi}")

    elif valinta == 4:
        pelaaja.keraa_esine()

    elif valinta == 5:
        inventaario()

    elif valinta == 6:
        lepaa()

    elif valinta == 7:
        print("Peli lopetetaan.")
        break

    else:
        print("Virheellinen valinta.")


"""Luo luokat: pelaaja, huone ja esine
esineiden ominaisuuksia ovat esim. nimi ja paino
pelaajan ominaisuuksia ovat ainakin nimi, lista hallussa olevista esineistä ja sijainti (huone, missä pelaaja kulloinkin on)
huoneen ominaisuuksia ovat nimi ja mahdollisesti esine
kun ohjelma käynnistetään, luodaan pelaajaolio ja muutama esine ja huone
pelaajan toimintoja ovat liikkuminen ja esineen kerääminen (ohjelman käyttäjä voi suorittaa niitä pelin valikosta, päivitä valikkoa tarpeen mukaan)"""
