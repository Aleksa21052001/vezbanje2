'''
Napisati program koji pita korisnika da unese nekoliko reči odvojenih zarezom, potom ispisuje reč po
reč, svaku u zasebnom redu. Unutar programa je potrebno razbiti uneseni string na listu stringova,
potom koristeći for petlju proći kroz listu.
'''


def main():
    tekst = input("Unesite reci odvojene zarezom: ")
    reci = tekst.split(",")

    for rec in range(len(reci)):
        print(reci[rec])


main()
