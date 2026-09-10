def bensa(gallona):
    litra = gallona * 3.785
    return litra

while True:
    gallon = float(input("Kerro gallona määrä\n"))
    if gallon < 0:
        break
    print(bensa(gallon))
