import time
import random

pelaajannimi = input("Mikä sinun nimesi on?\n")
pelaajanikä = input(f"Hauska tavata {pelaajannimi}! Mikä sinun ikäsi on?\n")


class Pelaaja:
    def __init__(self, nimi, esinelista, sijainti):
        self.nimi = nimi
        self.esinelista = esinelista
        self.sijainti = sijainti

    def liiku(self, seuraava_huone):
        self.sijainti = seuraava_huone

    def keraa_esine(self):
        if self.sijainti.esine is not None:
            self.esinelista.append(self.sijainti.esine)
            print(f"Keräsit esineen: {self.sijainti.esine.nimi}")
            self.sijainti.esine = None
        else:
            print("Tässä huoneessa ei ole esinettä.")


class Huone:
    def __init__(self, nimi, esine):
        self.nimi = nimi
        self.esine = esine


class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino


def inventaario():
    while True:
        print("=== Inventaario ===")

        if len(pelaaja.esinelista) == 0:
            print("Inventaario on tyhjä!")
        else:
            for esine in pelaaja.esinelista:
                print(f"{esine.nimi}, paino: {esine.paino} g")

        valinta = input("1. Takaisin päävalikkoon\nValitse: ")

        if valinta == "1":
            break


def lepaa():
    print("Menit nukkumaan likaiseen ja pölyiseen sänkyyn...")
    uniaika = 5

    while uniaika != 0:
        time.sleep(1)
        print("zZzZzZzZ...")
        uniaika = uniaika - 1

    if random.randint(1, 2) == 1:
        print("Heräsit kesken yön oksentamaan ja tunsit itsesi sairaaksi. :(")
        time.sleep(2)
        print("Sairastuit ja päätit lähteä mökistä. Peli päättyi...")
        exit()
    else:
        print("Heräsit virkeänä! :)")

    time.sleep(3)


# Luodaan esineet

avaimet = Esine("vanha avain", 10)
Einon_kirje = Esine("Einon kirje", 5)
vanha_valokuva = Esine("vanha valokuva", 20)
sorkkarauta = Esine("sorkkarauta", 1500)
vanha_vihko = Esine("vanha vihko", 150)
huolto_avain = Esine("Huolto laatikon avain", 200)

huolto_laatikko_avattu = False
pohjapiirros_luettu = False
luukku_löytynyt = False
luukku_avattu = False
kellari_tutkittu = False

# Luodaan huoneet
eteinen = Huone("Eteinen", None)
keittio = Huone("Keittiö", None)
olohuone = Huone("Olohuone", vanha_vihko)
makuuhuone = Huone("Makuuhuone", huolto_avain)
vaja = Huone("Vaja", sorkkarauta)
piha = Huone("Piha", None)
takapiha = Huone("Mökin takapiha", None)
kellari = Huone("Kellari", None)
viimeinen_huone = Huone("Viimeinen huone", None)

# Luodaan pelaaja
inventaario1 = []

pelaaja = Pelaaja(pelaajannimi, inventaario1, piha)

print(f"{pelaajannimi} saa kirjeen...")
print("Hei.")
time.sleep(1)
print("Et tunne minua, mutta olen jättänyt sinulle mökin.")
time.sleep(1)
print("Älä kysy miksi.")
time.sleep(1)
print("Mökki sijaitsee järven rannalla, noin 40 km kaupungista.")
time.sleep(1)
print("Avaimet ovat postilaatikossa.")
time.sleep(1)
print("Yksi asia vielä:")
time.sleep(1)
print("Älä mene kellariin.")
time.sleep(1)
print("Terveisin,")
time.sleep(1)
print("Eino")
time.sleep(2)
print(f"{pelaajannimi} sanoo: 'Kuka ihme on Eino? Miksi hän jätti minulle mökin? Miksi en saa mennä kellariin?'")
time.sleep(1)
print(f"{pelaajannimi} sanoo: 'No, ei auta muu kuin mennä mökille ja selvittää asia.'")
input("Paina enter jatkaaksesi...")
print("Olet saapunut mökin pihalle.\n")
print("Edessäsi on vanha mökki.")
print("Vieressä on vaja.")
print("Takana on metsä.")

print("Postilaatikko näyttää siltä, ettei sitä ole avattu ainakaan kymmeneen vuoteen.")
while True:
    print("\n=== Päävalikko ===")
    print(f"Olet paikassa: {pelaaja.sijainti.nimi}")
    if pelaaja.sijainti.esine is not None:
        print(f"paikassa on esine: {pelaaja.sijainti.esine.nimi}")

    if pelaaja.sijainti == piha:
        print("1. Mene mökkiin")
        print("2. Tutki pihaa")
        print("3. Tutki postilaatikkoa")
        print("4. Mene vajaan")
        print("5. Mene mökin takapihalle")

    elif pelaaja.sijainti == eteinen:
        print("1. Mene keittiöön")
        print("2. Mene olohuoneeseen")
        print("3. Tutki sähkökaappia")
        print("4. Mene takaisin pihalle")

    elif pelaaja.sijainti == keittio:
        print("1. Mene eteiseen")
        print("2. Mene olohuoneeseen")

    elif pelaaja.sijainti == olohuone:
        print("1. Mene keittiöön")
        print("2. Mene eteiseen")
        print("3. Mene makuuhuoneeseen")
        print("4. Tutki vanhaa valokuvaa")
        print("5. Mene kellariin")
        print("6. Kerää esine")
        if vanha_vihko in pelaaja.esinelista:
            print("7. Tutki vanhaa vihkoa")

    elif pelaaja.sijainti == makuuhuone:
        print("1. Tutki makuuhuonetta")
        print("2. Nuku sängyllä")
        print("3. Kerää esine")
        print("4. Mene takaisin olohuoneeseen")
        if huolto_laatikko_avattu:
            print("5. Tutki yöpöydän papereita")

    elif pelaaja.sijainti == vaja:
        print("1. Tutki vajaa")
        print("2. Avaa huolto laatikko")
        print("3. Kerää esine")
        print("4. Mene takaisin pihalle")

    elif pelaaja.sijainti == kellari:
        print("1. Tutki kellaria")
        print("2. Tutki alkuperäistä kellarin ovea")
        print("3. Tutki putkia")
        print("4. Mene takaisin portaille")

    elif pelaaja.sijainti == takapiha:
        print("1. Tutki mökin takapihaa")
        if not luukku_löytynyt:
            print("2. Mene takaisin pihalle")
        elif luukku_löytynyt and not luukku_avattu:
            print("2. Avaa luukku")
            print("3. Mene takaisin pihalle")
        elif luukku_avattu:
            print("2. Mene kellariin")
            print("3. Mene takaisin pihalle")

    elif pelaaja.sijainti == viimeinen_huone:
        print("1. Tutki huonetta")
        print("2. Avaa kirjekuori")
        print("3. Lähde pois")

    valinta = int(input("Valitse: "))

#pihan toiminnot
    if pelaaja.sijainti == piha:
        if valinta == 1:
            if avaimet in pelaaja.esinelista:
                print("Mökin ovi on lukossa. Sinulla on avaimet, joten avaat oven.")
                pelaaja.liiku(eteinen)
            else:
                print("Mökin ovi on lukossa. Sinulla ei ole avaimia, joilla mennä sisään.")
        elif valinta == 2:
            print("Tutkit pihaa...")
            time.sleep(2)
            print("Pihalla ei näytä olevan mitään mielenkiintoista.")
            time.sleep(2)
        elif valinta == 3:
            print("Tutkit postilaatikkoa ja löysit avaimet mökkiin.")
            print("Avaimet lisättiin inventaarioosi.")
            pelaaja.esinelista.append(avaimet)
        elif valinta == 4:
            pelaaja.liiku(vaja)
        elif valinta == 5:
            pelaaja.liiku(takapiha)
        else:
            print("Virheellinen valinta.")

#vajan toiminnot
    elif pelaaja.sijainti == vaja:
        if valinta == 1:
            print("Tutkit vajaa...")
            time.sleep(2)
            print("Vaja on täynnä vanhoja työkaluja joita ei voi edes käyttää enään.")
            time.sleep(2)
            print("Nurkkassa on vanha aurinkopaneeli.")
            time.sleep(2)
            print("Sen vieressä on lappu:")
            print('"Toimii vielä, jos joku jaksaa korjata."')
            time.sleep(2)
            print("Silmäsi kiinnittyy metalliseen esineeseen, joka näyttää sorkkarauttalta. se on pölyinen ja ruosteinen")
            time.sleep(2)
            print("Vajan pimeässä nurkassa on laatikko jonka päällä lukee 'KELLARIN HUOLTO'")
            input("Paina enter jatkaaksesi...")
        elif valinta == 2:
            if huolto_avain in pelaaja.esinelista:
                huolto_laatikko_avattu = True
                print("Kaivat taskustasi huolto laatikon avaimen ja avaat laatikon.")
                time.sleep(2)
                print("Laatikon sisältä löytyy vanha paperi.")
                time.sleep(1)
                print("Paperissa lukee: 'Kellarin ovi ei ole koskaan ollut tarkoitettu avattavaksi ulkopuolelta.'")
                time.sleep(2)
                print("Paperin alareunassa on pieni piirros mökistä")
                print("Piirroksessa on kellarin kohdalla ympyrä")
                print("Sen vieressä lukee pienellä käsialalla: 'etsi toinen reitti.'")
            else:
                print("Laatikko on lukossa. Lukko näyttää vanhalta mutta melko tukevalta.")
        elif valinta == 3:
            print("sanot 'pyh onpa likainen sorkkarauta' ja pyyhit sen pölystä ja ruosteesta. Se näyttää käyttökelpoiselta")
            pelaaja.keraa_esine()
        elif valinta == 4:
            pelaaja.liiku(piha)
        else:
            print("Virheellinen valinta.")

#eteisen toiminnot
    elif pelaaja.sijainti == eteinen:
        if valinta == 1:
            pelaaja.liiku(keittio)
        elif valinta == 2:
            pelaaja.liiku(olohuone)
        elif valinta == 3:
            print("Tutkit sähkökaappia...")
            time.sleep(2)
            print("Sähkökaappi on todella vanha.")
            print("Yksi sulake näyttää palaneelta")
            time.sleep(2)
        elif valinta == 4:
            pelaaja.liiku(piha)
        else:
            print("Virheellinen valinta.")

#olohuoneen toiminnot
    elif pelaaja.sijainti == olohuone:
        if valinta == 1:
            pelaaja.liiku(keittio)
        elif valinta == 2:
            pelaaja.liiku(eteinen)
        elif valinta == 3:
            pelaaja.liiku(makuuhuone)
        elif valinta == 4:
            print("Tutkit vanhaa valokuvaa...")
            time.sleep(1)
            print("Kuvassa on vanha mökki ja sen edessä seisoo mies.")
            time.sleep(1)
            print("Kuvan takana lukee: 'Eino ja mökki, kesä 1995'")
        elif valinta == 5:
            print("Nykäset kellarin ovea kovaa mutta ovi ei liikahdakaan.")
            print("Kellarin oveen on asennettu vahvistettu lukko. Et saa sitä auki ilman avainta.")
        elif valinta == 6:
            pelaaja.keraa_esine()
        elif valinta == 7:
            if vanha_vihko in pelaaja.esinelista:
                print("Avasit vanhan vihkon...")
                time.sleep(1)
                print("'12.6.1995'")
                print("'Korjasin katon. Kaikki näyttää hyvältä. Huomenna tulen mökille pitämään vapaapäivän.'")
                time.sleep(1)
                print("'13.6.1995'")
                print("'Kävin järvellä. Sain saaliiksi kolme kalaa. Aion tehdä niistä herkullisen aterian.'")
                time.sleep(1)
                print("'19.6.1995'")
                print("'Kuulin taas ääniä kellarista.'")
                time.sleep(1)
                print("'20.6.1995'")
                print("'Todennäköisesti äänet kuuluvat putkista jotka menee kellariin. Käyn katsomassa putkia huomenna.'")
                time.sleep(1)
                print("Kulmakarvasi kohoavat kun avaat seuraavan sivun.")
                time.sleep(1)
                print("----------------------------------")
                print("KELLARI\nkellari kellari kellari\nÄLÄ AVAA ÄLÄ AVAA ÄLÄ AVAA\nseonsiellä\noven takana\nkellari\nkellari\nKELLARI\nälä avaa\nse ei ole putket\n se ei ole putket\nse ei ole putket\n....\nVaja.\nKatso vajasta.")          
                print("----------------------------------")
                time.sleep(5)
                print("Sivun alareunaan on piirretty kuva kellarin ovesta jossa on raapimajälkiä.")
                print("Oven ympärille on piirretty useampi nuoli joka osoittaa ovea päin.")
                time.sleep(1)
                print("Vihko jatkuu yllättäen tämän sivun jälkeen normaalein muistiinpanoin 1998 vuoteen saakka ilman mitään mainintaa kellarista.")
        else:
            print("Virheellinen valinta.")

#makuuhuoneen toiminnot
    elif pelaaja.sijainti == makuuhuone:
        if valinta == 1:
            print("Tutkit makuuhuonetta...")
            time.sleep(1)
            print("Sänky on vanha ja pölyinen.")
            time.sleep(2)
            print("Yöpöydällä on kasa vanhoja papereita.")
            time.sleep(2)
            print("Maton alta pilkottaa jotain metallista.")
        elif valinta == 2:
            lepaa()
        elif valinta == 3:
            pelaaja.keraa_esine()
        elif valinta == 4:
            pelaaja.liiku(olohuone)
        elif valinta == 5 and huolto_laatikko_avattu:
            pohjapiirros_luettu = True
            print("Tutkit yöpöydän papereita... Suurin osa käsittelee vanhoja laskuja tai mökin huoltoa.")
            print("Yksi paperi kuitenkin kiinnittää huomiosi.")
            time.sleep(1)
            print("Paperiin on piirretty mökin pohjapiirros.")
            print("Kellarin kohdalla näkyy kaksi sisäänkäyntiä. Toinen on kellarin ovi, mutta toinen on mökin ulkopuolella.")
        else:
            print("Virheellinen valinta.")

#takapihan toiminnot
    elif pelaaja.sijainti == takapiha:
        if valinta == 1:
            print("Tutkit mökin takapihaa...")
            time.sleep(2)

            if pohjapiirros_luettu:
                print("Muistat pohjapiirroksen.")
                print("Siinä kellarin toinen sisäänkäynti näytti olevan juuri täällä.")
                time.sleep(2)
                print("Siirrät vanhoja lautoja sivuun.")
                print("Niiden alta paljastuu pieni metallinen luukku.")
                luukku_löytynyt = True
            else:
                print("Täällä on paljon korkeaa ruohoa ja vanhoja lautoja.")
                time.sleep(2)
                print("Yksi kohta maan pinnassa näyttää kuitenkin oudolta.")

        elif valinta == 2:
            if not luukku_löytynyt:
                pelaaja.liiku(piha)

            elif luukku_löytynyt and not luukku_avattu:
                if sorkkarauta in pelaaja.esinelista:
                    print("Tutkit metallista luukkua.")
                    time.sleep(2)
                    print("Luukku on ruostunut kiinni.")
                    time.sleep(1)
                    print("Tarvitset jonkin työkalun sen avaamiseen.")
                    print("Kaivat sorkkaraudan esiin.")
                    time.sleep(2)
                    print("Väännät luukkua voimakkaasti...")
                    time.sleep(2)
                    print("KRRRRAAAAK!")
                    time.sleep(2)
                    print("Luukku aukeaa.")
                    luukku_avattu = True
                else:
                    print("Luukku on jumissa.")
                    print("Tarvitsisit jonkin työkalun sen avaamiseen.")

            elif luukku_avattu:
                print("Katsot pimeisiin portaisiin.")
                time.sleep(2)
                print("Portaat näyttävät johtavan suoraan kellariin.")
                time.sleep(2)
                print("Astut alas...")
                time.sleep(2)
                pelaaja.liiku(kellari)

        elif valinta == 3:
            pelaaja.liiku(piha)

        else:
            print("Virheellinen valinta.")

# kellarin toiminnot
    elif pelaaja.sijainti == kellari:
        if valinta == 1:
            kellari_tutkittu = True
            print("Tutkit kellaria...")
            time.sleep(2)
            print("Kellari on paljon suurempi kuin ulkoa voisi olettaa.")
            time.sleep(2)
            print("Seinät ovat kosteita ja ilma tuntuu kylmältä.")
            time.sleep(2)
            print("Lattialla on paksu kerros pölyä.")
            time.sleep(2)
            print("Jotain outoa kuitenkin huomaat.")
            print("Pölyssä näkyy tuoreita jalanjälkiä.")
            time.sleep(2)
            print("Joku on käynyt täällä hiljattain...")

        elif valinta == 2:
            print("Tutkit vanhaa kellarin ovea...")
            time.sleep(2)
            print("Tämä on sama ovi, jota yritit avata olohuoneesta.")
            time.sleep(2)
            print("Ovi näyttää sisältäpäin paljon vanhemmalta.")
            time.sleep(2)
            print("Oven vieressä seinässä on pieniä naarmuja.")
            time.sleep(2)
            print("Niiden alla näkyy jotain kirjoitettuna.")
            print("'Älä koskaan avaa tätä ovea.'")
            print("Mietit että miksi sisältäkään päin ovea ei saa avata..")

        elif valinta == 3:
            if kellari_tutkittu:
                print("Tutkit kellarin putkia...")
                time.sleep(2)
                print("Seinää pitkin kulkee useita vanhoja metalliputkia.")
                time.sleep(2)
                print("Yksi niistä näyttää paljon uudemmalta kuin muut.")
                time.sleep(2)
                print("Se johtaa syvemmälle kellariin.")
                time.sleep(2)
                print("Kuulet putken sisältä hiljaisen kolahduksen.")
                print("Klonk.")
                time.sleep(2)
                print("Huomaat putken takana pienen oven.")
                time.sleep(2)
                print("Ovi näyttää johtavan johonkin kellarin ulkopuolella olevaan huoneeseen.")
                time.sleep(2)
                print("Avaat oven...")
                time.sleep(2)
                pelaaja.liiku(viimeinen_huone)
            else:
                print("Ehkä sinun pitäisi ensin tutkia kellaria tarkemmin.")

        elif valinta == 4:
            print("Nouset takaisin portaita.")
            time.sleep(2)
            pelaaja.liiku(takapiha)

        else:
            print("Virheellinen valinta.")

"""Luo luokat: pelaaja, huone ja esine
esineiden ominaisuuksia ovat esim. nimi ja paino
pelaajan ominaisuuksia ovat ainakin nimi, lista hallussa olevista esineistä ja sijainti (huone, missä pelaaja kulloinkin on)
huoneen ominaisuuksia ovat nimi ja mahdollisesti esine
kun ohjelma käynnistetään, luodaan pelaajaolio ja muutama esine ja huone
pelaajan toimintoja ovat liikkuminen ja esineen kerääminen (ohjelman käyttäjä voi suorittaa niitä pelin valikosta, päivitä valikkoa tarpeen mukaan)"""
