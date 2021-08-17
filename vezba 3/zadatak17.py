'''
Napiši program koji izračunava zbir brojeva koje unosi korisnik. Prvo je potrebno uneti
broj brojeva koje treba sabrati. Potom treba uneti sve brojeve i na kraju ispisati vrednost zbira.
'''


def main():
    n = eval(input("Unesite n: "))
    zbir = 0

    for i in range(n):
        broj = float(input("Unesite broj: "))
        zbir = zbir + broj

    print("Ukupan zbir iznosi: ", zbir)


main()
