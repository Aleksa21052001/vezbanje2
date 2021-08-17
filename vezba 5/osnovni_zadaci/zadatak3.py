"""
Napisati funkciju koja kao parametar neki broj n. Funkcija treba da kao povratnu vrednost vrati zbir prvih n
prirodnih brojeva.
"""


def zbir_prirodnih_brojeva(n):
    zbir = 0
    for broj in range(1, n+1):
        zbir = zbir + broj

    return zbir


print(zbir_prirodnih_brojeva(10))
