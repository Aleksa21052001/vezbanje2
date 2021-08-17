"""
Napiši funkciju koji datum prima u obliku dd/mm/gggg i proverava da li je datum validan. Na
primer 24/5/1962 je validan datu, ali 31/9/2000 nije jer septembar nema 31 dan. Takođe voditi računa i
o tome da li je godina prestupna.
"""


def prestupna_godina(godina):
    if godina % 4 == 0:
        if godina % 100 == 0:
            if godina % 400 == 0:
                return True
        else:
            return True

    return False


def proveri_datum(datum):
    broj_dana_u_mesecu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    datum_split = datum.split("/")
    dan = int(datum_split[0])
    mesec = int(datum_split[1])
    godina = int(datum_split[2])

    if prestupna_godina(godina):
        broj_dana_u_mesecu[1] = 29

    if 0 < mesec <= 12:
        if 0 < dan <= broj_dana_u_mesecu[mesec - 1]:
            return True
    return False


print(proveri_datum('29/2/2000'))
