"""
Napiši funkciju koja prima broj bodova na testu, a vraća ocenu sa testa. Student na testu
može da osvoji od 0 do 100 bodova.

bodovi         ocena
--------------------
od 0 do 55     5
od 56 do 65    6
od 66 do 75    7
od 76 do 85    8
od 86 do 95    9
od 96 do 100   10
--------------------
"""


def ocenjivanje(broj_bodova):

    if broj_bodova <= 55:
        print("5")
    elif broj_bodova > 55 and broj_bodova <= 65:
        print("6")
    elif broj_bodova > 65 and broj_bodova <= 75:
        print("7")
    elif broj_bodova > 75 and broj_bodova <= 85:
        print("8")
    elif broj_bodova > 85 and broj_bodova <= 95:
        print("9")
    elif broj_bodova > 95:
        print("10")


ocenjivanje(96)
