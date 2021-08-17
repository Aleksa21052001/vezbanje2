'''
Napiši program koji izračunava zbir kvadrata prvih n prirodnih brojeva, gde se n unosi sa
tastature.
'''


def main():
    zbir = 0
    n = eval(input("Unesite n: "))

    for i in range(1, n+1):
        zbir = zbir + i**2

    print("Ukupan zbir iznosi: ", zbir)


main()
