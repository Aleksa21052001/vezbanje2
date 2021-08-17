"""
Napiši program koji prima datum u obliku dd/mm/gggg i računa redni broj dana u godini.

Redni broj dana u godini se računa na sledeći način:
1. danUGodini = 31(mm - 1) + dd
2. ako je mm posle februara danUGodini umanji za (4mm+23)/10
3. ako je prestupna godina i mm posle februara danUGodini uvećaj za 1

Ocekuje se da unosite validan datum. Ukoliko zelite mozete iskoristiti funkciju iz prethodnog zadatka da
proverite ispravnost datuma.
"""


def prestupna_godina(godina):
    if godina % 4 == 0:
        if godina % 100 == 0:
            if godina % 400 == 0:
                return True
        else:
            return True

    return False


def izracunaj_dan_u_godini(datum):
    datum_split = datum.split("/")
    dan = int(datum_split[0])
    mesec = int(datum_split[1])
    godina = int(datum_split[2])

    dan_u_godini = 31 * (mesec - 1) + dan

    if mesec > 2:
        dan_u_godini -= (4*mesec + 23) // 10

    if prestupna_godina(godina) and mesec > 2:
        dan_u_godini += 1

    return dan_u_godini


print(izracunaj_dan_u_godini('14/11/2020'))
