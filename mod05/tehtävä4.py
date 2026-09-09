import random
luku = random.randint(0, 10)
while True:

    luku1 = input("Arvaa luku 0-10")

    if luku > int(luku1):
        print("Liian pieni arvaus")
    if luku < luku1:
        print("Liian suuri arvaus")
    if luku == int(luku1):
        print("Oikein")
        break
