"""
Napiši program za registrovanje korisnika. Program teba da omogući korisniku da unese
korisničko ime i lozinku. Informacije o korisniku čuvaju se u tekstualnom fajlu.
"""

def main():
    f=open("registrovanje-korisnika.txt", "a")

    ime = input("ime: ")
    sifra = input("sifra: ")

    podaci= f"{ime}|{sifra}"

    f.write(podaci)

    f.close()


def registracija():
    korisnicko_ime = input("korisnicko ime: ")
    lozinka = input("lozinka: ")
    podaci_o_korisniku = korisnicko_ime + "|" + lozinka + "\n"

    f = open("korisnici.txt", "a")
    f.write(podaci_o_korisniku)
    f.close()

registracija()

