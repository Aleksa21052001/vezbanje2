'''
Napiši program koji izračunava prosek brojeva koje unosi korisnik (slično prethodnom
zadatku). Prosek bi trebalo da bude float.
'''


def main():
    n = eval(input("Unesite n: "))
    zbir = 0

    for i in range(n):
        broj = float(input("Unesite broj: "))
        zbir = zbir + broj

    prosek = zbir / n
    print("Prosek je: ", prosek)


main()
