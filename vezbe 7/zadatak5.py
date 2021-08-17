"""
Napiši funkciju koja prima prirodni broj n, a vraća listu koja sadrži sve proste brojeve koji su
manji od n.
"""


def prost_broj(broj):
    koren = int(broj**0.5)

    if koren <= 2:
        return broj % 2 != 0 or broj == 2

    for i in range(2, koren):
        if broj % i == 0:
            return False
    return True


def prosti_brojevi(n):
    brojevi = []

    for broj in range(1, n+1):
        if prost_broj(broj):
            brojevi.append(broj)

    return brojevi


print(prosti_brojevi(30))
