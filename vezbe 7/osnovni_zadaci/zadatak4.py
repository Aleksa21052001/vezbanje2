"""
Napisati program koji pita korisnika da pogađa broj. Ispravan broj koji korisnik treba da pogodi je broj 42.
Program pita korisnika da unese broj sve dok ne unese tačan broj. Ukoliko je broj netačan, program kaže
korisniku da li je pravi broj manji ili veći od unetog.
"""


def main():
    while True:
        broj = int(input("unesite broj: "))

        if broj == 42:
            print("Tacan broj!")
            break
        elif broj > 42:
            print("Pravi broj je manji!")
        else:
            print("Pravi broj je veci!")


main()
