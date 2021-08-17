"""
Napiši funkciju koja čita iz fajla korisnička imena i lozinke i pročitane vrednosti vraća kao
listu. Prilikom poziva funkcije prosleđuje se naziv fajla i delimiter kojim je u fajlu korisničko ime odvojeno
od lozinke. Pri tome je element liste koja se vraća lista u kojoj je prvi element korisničko ime, a drugi
element lozinka.
"""


def citanje_iz_fajla(datoteka, delimiter):
    f = open(datoteka)
    redovi = f.readlines()
    #print(redovi)



    korisnici = []
    for red in redovi:
        korisnik = red.strip().split(delimiter)
        korisnici.append(korisnik)
        #print(korisnik)

    f.close()

    return korisnici


print(citanje_iz_fajla('korisnici.txt', '|'))
