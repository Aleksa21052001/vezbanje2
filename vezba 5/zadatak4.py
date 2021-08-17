"""
Napiši funkciju za registrovanje korisnika. Funkcija prima korisničko ime, lozinku, naziv fajla u
koji se snima i delimiter kojim će biti razdvojeno korisničko ime i lozinka. Korisničko ime i lozinku se
snimaju u fajl sa zadatim nazivom. Ta funkcija vraća korisnička imena i lozinke svih registrovanih
korisnika, kao što je specificirano u zadatku 3.
"""

def main(korisnicko_ime  , lozinka, file_path, delimiter):

    f = open(file_path, "r+")

    redovi = f.readlines()
    korisnici = korisnicko_ime + delimiter + lozinka+ "\n"
    f.write(korisnici)





    lista_korisnika = []
    for red in redovi:
        korisnik = red.strip().split(delimiter)
        lista_korisnika.append(korisnik)

    f.close()

    return lista_korisnika



x = main('marko', 'markovic', 'korisnici.txt', '|')

print(x)

def upis_u_fajl(korisnicko_ime, lozinka, datoteka, delimiter):
    f = open(datoteka, "r+")

    redovi = f.readlines()
    f.write(korisnicko_ime + delimiter + lozinka + "\n")
    f.close()

    korisnici = []
    for red in redovi:
        korisnik = red.strip().split(delimiter)
        korisnici.append(korisnik)

    korisnici.append([korisnicko_ime, lozinka])

    return korisnici


