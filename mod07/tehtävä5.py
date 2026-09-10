def parillinen(lista):
    karsittulista = []
    for pariton in lista:
        if pariton % 2 == 0:
            karsittulista.append(pariton)
    return karsittulista


numeroita = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"alkuperäinen lista: {numeroita}, parillinen lista: {parillinen(numeroita)}")