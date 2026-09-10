import random
def noppaluku():
    noppa = random.randint(1, 6)
    return noppa

noppa = noppaluku()

while noppa != 6:
    print(noppa)
    noppa = noppaluku()

print(noppa)