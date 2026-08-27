yhtkg = 0
luoti1 = 13.3
naula1 = 32 * luoti1
leiviskä1 = 20 * naula1


leiviskä = float(input("Anna leiviskät.\n"))

naula = float(input("Anna  naulat.\n"))

luoti = float(input("Anna luodit.\n"))
luoti2 = luoti1 * luoti
naula2 = naula1 * naula
leiviskä2 = leiviskä1 * leiviskä

yht = luoti2 + naula2 + leiviskä2
while yht >= 1000:
    yht = yht - 1000
    yhtkg = yhtkg + 1
print (f"Massa nykymittojen mukaan:\n{yhtkg} kilogrammaa ja {yht:.2f} grammaa.")