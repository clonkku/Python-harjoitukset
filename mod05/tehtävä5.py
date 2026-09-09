yritykset = 0

while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break

    yritykset += 1

    if yritykset == 5:
        print("Pääsy evätty")