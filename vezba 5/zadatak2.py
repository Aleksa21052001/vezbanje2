"""
 Napiši program koji za zadati niz brojeva:
• Ispisuje najmanji element niza
• Ispisuje najveći element niza
• Ispisuje sumu vrednosti u nizu
• Ispisuje srednju vrednost za niz
Svaki od zadatih zahteva trebada bude implementiran kao posebna funkcija.
"""


def najmanji_element_niza(niz):
    najmanji_element = niz[0]

    for element in niz:
        if element < najmanji_element:
            najmanji_element = element

    print("najmanji element niza je: ", najmanji_element)


def najveci_element_niza(niz):
    najveci_element = niz[0]

    for element in niz:
        if element > najveci_element:
            najveci_element = element

    print("najveci element niza je: ", najveci_element)


def suma_elemenata_niza(niz):
    suma = 0

    for element in niz:
       suma = suma + element

    print("suma elemenata niza je: ", suma)


def prosek_elemenata_niza(niz):
    suma = 0
    n = len(niz)
    for element in niz:
       suma = suma + element

    print("prosek elemenata niza je: ", suma/n)


def karakteristike_niza(niz):
    najmanji_element_niza(niz)
    najveci_element_niza(niz)
    suma_elemenata_niza(niz)
    prosek_elemenata_niza(niz)


karakteristike_niza([1,2,3,4,5,-1,6])
