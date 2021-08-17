"""
Godina je prestupna ako je deljiva sa 4, osim ako je poslednja godina u veku, a tada je
prestupna ako je deljiva sa 400 (na primer 1800 i 1900 nisu prestupne dok 1600 i 2000 jesu). Napisati
funkciju koji proverava da li je godina prestupna.
"""


def prestupna_godina(godina):
    if godina % 4 == 0:
        if godina % 100 == 0:
            if godina % 400 == 0:
                return 'Prestupna je!'
        else:
            return 'Prestupna je!'

    return 'Nije prestupna!'


print(prestupna_godina(1800))
