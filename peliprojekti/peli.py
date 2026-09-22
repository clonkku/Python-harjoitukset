import time
import random
pelaajannimi = input("Mikä sinun nimesi on?\n")
pelaajanikä = input(f"Hauska tavata {pelaajannimi}! Mikä sinun ikäsi on?\n")

inventaario1 = []

def lisaaesine():
    esine = input("Minkä esineen haluat lisätä inventaarioon?: ")
    inventaario1.append(esine)
    return

def inventaario():
    while True:
        print("=== Inventaario ===")
        if len(inventaario1) == 0:
            print("inventaario on tyhjä!")
        else:
            print(inventaario1)

        valinta = input("1. Takaisin päävalikkoon\nValitse:")
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
        print(r"""                .-""""""-.
           .'  \\  //  '.
          /   O      O   \ 
         :                :
         |                |  
         :       __       :
          \  .-"`  `"-.  /
           '.          .'
             '-......-'""")
    else:
        print("Heräsit virkeänä! :)")
    time.sleep(3)
    return

while True:
    print("=== Päävalikko ===\n" \
    "1. Lisää esine\n" \
    "2. Näytä inventaario\n" \
    "3. Nuku")
    valinta = int(input("Valitse: "))
    if valinta == 1:
        lisaaesine()
    elif valinta == 2:
        inventaario()
    elif valinta == 3:
        lepaa()

