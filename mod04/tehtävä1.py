# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, 
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.
pituus = float(input("Mikä on kuhan pituus?\n"))
alamitta = 37
if pituus < alamitta:
    pituus = alamitta - pituus
    print(f"kuha on {pituus} cm alamittainen, laske kuha takaisin järveen")