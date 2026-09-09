sukupuoli = input("Mikä on sinun biologinen sukupuoli?\n")
hemoglobiini = float(input("Mikä on sinun hemoglobiiniarvo (g/l)\n"))
if sukupuoli == "mies" or sukupuoli == "poika":
    if hemoglobiini < 134:
        print("Hemoglobiini tasosi on alhainen")
    elif 134 <= hemoglobiini <= 195:
        print("Hemoglobiini tasosi on normaali")
    elif hemoglobiini > 195:
        print("Hemoglobiini tasosi on korkea")
    else:
        print("Väärä hemoglobiiniarvo")
elif sukupuoli == "nainen" or sukupuoli == "tyttö":
    if hemoglobiini < 117:
        print("Hemoglobiini tasosi on alhainen")
    elif 117 <= hemoglobiini <= 175:
        print("Hemoglobiini tasosi on normaali")
    elif hemoglobiini > 175:
        print("Hemoglobiini tasosi on korkea")
    else:
        print("Väärä hemoglobiiniarvo")
else:
    print("Virheellinen sukupuoli")


