"""Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, 
jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan."""
def summa(lista):
    apua = 0
    for numero in lista:
        apua = apua + numero
    return apua

testilista = [1, 2, 3, 4]
print(summa(testilista))
