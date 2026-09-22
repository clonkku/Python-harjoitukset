class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros

    def siirry_kerrokseen(self, kerrokseen):
        while  self.kerros != kerrokseen:
            if kerrokseen > self.kerros:
                self.kerros_ylos()
            if kerrokseen < self.kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        self.kerros = self.kerros + 1
        print(f"olet kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros = self.kerros - 1
        print(f"olet kerroksessa {self.kerros}")


class Talo:
    def __init__(self, alinkerros, ylinkerros, hissi_maara):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissilista = []

        for i in range(hissi_maara):
            hissi1 = Hissi(alinkerros, ylinkerros)
            self.hissilista.append(hissi1)

    def aja_hissia(self, hissinro, kohdekerros):
        self.hissilista[hissinro-1].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        for hissit in self.hissilista:
            hissit.siirry_kerrokseen(self.alinkerros)


talo = Talo(1, 10, 5)
talo.aja_hissia(1, 5)        
talo.aja_hissia(2, 9)
talo.aja_hissia(3, 4)

talo.palohalytys()
