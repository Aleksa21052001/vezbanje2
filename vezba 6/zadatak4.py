"""
Kazna za brzu vožnju računa se kao 5000 din + 500 din za svaki kilometar preko ograničenja +
10000 din za vožnju preko 120km/h. Napisati funkciju koja prima izmerenu brzinu vozila i ograničenje
brzine. Ako je brzina veća od dozvoljene funkcija vraća poruku sa cenom kazne, a ako je manja vraća
poruku da je sve u redu.
"""


def kazna(brzina, ogranicenje):

    if brzina <= ogranicenje:
        print("Niste prekoracili brzinu!")
    else:
        iznos = 5000 + (brzina - ogranicenje)*500

        if brzina > 120:
            iznos += 10000

        print("Vasa kazna iznosi:", iznos, "rsd.")


kazna(121.4, 35)
