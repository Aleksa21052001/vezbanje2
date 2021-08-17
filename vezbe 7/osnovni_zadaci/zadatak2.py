"""
Napisati program za login korisnika na sistem. Program treba da pita korisnika da unese korisničko ime i šifru
sve dok korisnik ne unese ispravno korisničko ime i šifru - doktorjoca i kartica4.
"""


def main():
    while True:
        korisnicko_ime = input("korisnicko ime: ")
        lozinka = input("lozinka: ")

        if korisnicko_ime == "doktorjoca" and lozinka=='kartica4':
            break


main()
