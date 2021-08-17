'''
Napiši program koji izračunava dužinu merdevina za datu visinu koju treba dostići i ugao
kojim se meri nagib me
'''
from math import sin


def main():
    visina = float(input("Unesite visinu: "))
    ugao = float(input("Uneiste ugao: "))

    duzina = visina/sin(ugao)

    print("Duzina merdevina iznosi:", duzina)


main()
