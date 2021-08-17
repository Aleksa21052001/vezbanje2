'''
Napisati program koji pita korisnika da unese jedan string i jedan broj n, potom ispisuje u jednom redu
taj string n puta.
'''


def main():
    string = input("Unesite string: ")
    broj = int(input("Unesite n: "))

    print("Vas string je: ", string * broj)


main()
