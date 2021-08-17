"""
Napisati program koji pita korisnika da unese nekoliko reči odvojenih razmakom, potom ispisuje iste te
reči, samo što umesto razmaka ih program spoji dvotačkom. Potrebno je koristiti funkcije split i join.
"""


def main():
    tekst = input("Unesite reci odvojene razmakom: ")
    reci = tekst.split(" ")
    novi_tekst = ":".join(reci)

    print(novi_tekst)


main()
