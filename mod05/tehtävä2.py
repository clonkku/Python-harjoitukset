#kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
while True:
    tuuma = float(input("Anna tuumamäärä"))
    if tuuma < 0:
        break
    print (tuuma * 2.54)