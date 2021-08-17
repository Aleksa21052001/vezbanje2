"""
Napiši funkciju koja prima inicijalnu vrednost x i vraća listu sa Sirakuza sekvencom za tu vrednost.
"""


def sirakuza(x):
    lista = [x]

    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3*x + 1
        lista.append(x)
    return lista


print(sirakuza(5))
