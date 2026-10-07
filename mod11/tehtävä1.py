class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja:
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

class Lehti:
    def __init__(self, paatoimittaja):
        self.paatoimittaja = paatoimittaja