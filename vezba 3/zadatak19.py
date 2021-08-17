'''
Napiši program koji izračunava aproksimaciju broja PI kao delimičnu sumu ovog reda:
4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ... Program treba da zatraži broj članova ovog niza koje treba sabrati.
'''


def main():
    n = eval(input("Unesite n: "))
    pi = 0
    for i in range(0, n):
        pi = pi + (4 / (2*i + 1) * (-1)**i)

    print("Aproksimacija broja PI je: ", pi)


main()
