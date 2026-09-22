#MODULE 9 CLASS, OBJECT AND CONSTRUCTOR
class Hero:
    sankarien_maara = 0

    def __init__(self, nimi, tyyppi, voima, aseaani, huudahdus="Hei!"):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.voima = voima
        self.aseaani = aseaani
        self.huudahdus = huudahdus
        Hero.sankarien_maara = Hero.sankarien_maara + 1    
    def huuda(self, kerrat=1):
        for i in range(kerrat):
            print(f"{self.huudahdus}")
        return
    def ase(self, kerrat=1):
        for i in range(kerrat):
            print(f"{self.aseaani}")
            return

hero1 = Hero("Reinhardt", "Tankki", "Voimakas", "pokspoks", "bonk")
hero2 = Hero("Tracer", "Vahingontekijä", "Nopea", "piupiupiu")
print(f"{hero1.nimi} on {hero1.tyyppi} ja hän on {hero1.voima}, hän sanoo {hero1.huudahdus}")
print(f"{hero2.nimi} on {hero2.tyyppi} ja hän on {hero2.voima}, hän sanoo {hero2.huudahdus}")

hero1.huuda()
hero1.ase()
hero2.huuda(2)
hero2.ase()