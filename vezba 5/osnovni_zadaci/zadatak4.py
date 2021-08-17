"""
Napisati funkciju koja kao parametar prima ime datoteke. Povratna vrednost funkcije treba da je promenljiva
tipa string koja sadrži prvi red te datoteke čije ime je funkcija dobila kao parametar.
"""


def procitaj_prvi_red(datoteka):
    f = open(datoteka)
    redovi = f.readlines()
    f.close()

    print(redovi)

    return redovi[0]


print(procitaj_prvi_red("korisnici.txt"))
