"""
Napisati funkciju koja prima dva parametra - korisničko ime i lozinku. Povratna vrednost funkcije je promenljiva
tipa boolean koja govori da li su korisničko ime i lozinka ispravni ili ne. Ukoliko je korisničko ime Marija,
a lozinka crno1234, funkcija treba da vrati True, u suprotnom treba da vrati False. Napisati program koji
traži od korisnika da unese korisničko ime i lozinku, poziva malopre napisanu funkciju koja proverava ispravnost
podataka, i koristeći povratnu vrednost funkcije obaveštava korisnika o tome da li su podaci ispravni ili ne.

"""

def prijava1(korisnicko_ime, lozinka):
    if korisnicko_ime == "Marija" and lozinka == "crno1234":
        return True
    return False

def main2():
    korisnicko_ime = input("ime ")
    lozinka = input("lozinka ")

    if prijava1(korisnicko_ime, lozinka):
        print("uneti podaci su ispravni")
    else:
        print("podaci su pogresani")

main2()




def prijava(korisnicko_ime, lozinka):
    if korisnicko_ime == 'Marija' and lozinka == 'crno1234':
        return True
    return False


def main():
    korisnicko_ime = input("korisnicko ime: ")
    lozinka = input("lozinka: ")

    if prijava(korisnicko_ime, lozinka):
        print("Uspesna prijava!")
    else:
        print("Pogresno korisnicko ime ili lozinka!")



