"""
Pozitivan ceo broj x veći od 2 je prost ako u intevalu [2, sqrt(x)] ne postoji ni jedan broj koji x
deli bez ostatka. Napiši funkciju koja proverava da li je broj prost. Funkcija treba da primi broj za koji se
proverava da li je prost, a da vrati True ako jeste, a False ako nije.
"""


def prost_broj(broj):
    koren = int(broj**0.5)

    if koren <= 2:
        return broj % 2 != 0 or broj == 2

    for i in range(2, koren):
        if broj % i == 0:
            return False
    return True


print(prost_broj(3))
