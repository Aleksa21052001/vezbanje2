"""
Zadatak 7. Napiši program za registrovanje novih proizvoda u prodavnici. Kada se program pokrene
prodavcu omogućuje jedino da se prijavi na sistem. Prilikom prijavljivanja na sistem prodavac unosi
korisničko ime i lozinku. Nakon što se uspešno prijavio na sitem, prodavac može da doda novi proizvod,
pri čemu unosi naziv, cenu i raspoloživu količinu proizvoda. Nakon što je dodat novi proizvod ispisuje se
spisak svih proizvoda u prodavnici. Dodavanje proizvoda se ponavlja dok prodavac ne unese „quit“.
Ukoliko prodavac unese „quit“ bilo za naziv, cenu ili količinu proizvoda, prekida se izvršavanje programa.
Korisnička imena i lozinke čuvaju se u fajlu prodavci.txt, a nazivi, cene i količine proizvoda čuvaju se u
fajlu proizvodi.txt.
"""
def ocitaj_proizvod():
    g = open("proizvodi.txt")

    redovi = g.readlines()

    for red in redovi:
        napisan_proizvod = red.strip().split("|")
        naziv_proizvoda = str(napisan_proizvod[0])
        cena_proizvoda = str(napisan_proizvod[1])
        kolicina_proizvoda = str(napisan_proizvod[2])

        print("proizvod:{} | njegova cena je: {} | kolicina proizvoda {}".format(naziv_proizvoda, cena_proizvoda, kolicina_proizvoda))

    g.close()

def novi_proizvod():
    f= open("proizvodi.txt", "a")


    print("")

    while True:
        f = open("proizvodi.txt", "a")
        naziv = input("unesite naziv proizvoda: ")
        if str(naziv)=="quit":
            break
        cena = input("cena proizvoda: ")
        if str(cena)=="quit":
            break
        kolicina = input("raspoloživa količina proizvoda: ")
        print("")
        if str(kolicina)=="quit":
            break

        proizvod = str(naziv)+"|"+str(cena)+"|"+str(kolicina)+"\n"
        f.write(proizvod)
        f.close()
        ocitaj_proizvod()


#novi_proizvod()

def mani():

    x=input("unesite ime: ")
    y=input("lozinka: ")
    print("dobro dosli na nalog, ukoliko zelite da prekinete unosa proizvoda ukucajte quit ")

    h = open("prodavci.txt", "a")
    prodavac = str(x) +"|"+str(y)+"\n"
    h.write(prodavac)

    h.close()

    novi_proizvod()

mani()






