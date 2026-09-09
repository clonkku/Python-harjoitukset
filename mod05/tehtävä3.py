luvut = []
while True:

    luku = input("Anna luku\n")
    if luku == "":
        break
   
    luvut.append(float(luku))
luvut.sort()
print(luvut[0])
print(luvut[-1])