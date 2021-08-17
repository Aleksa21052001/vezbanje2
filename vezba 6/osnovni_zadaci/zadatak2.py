"""
Napisati program koji traži od korisnika da unese jedan broj. Ukoliko je broj veći od deset, program treba da
ispiše korisniku Broj je velik!, a ukoliko je manji od deset, treba da ispiše Broj nije velik!.
"""


def main():
    broj = int(input("unesite broj: "))

    if broj > 10:
        print("Broj je velik!")
    else:
        print("Broj nije velik!")


main()
