"""
Koristeći while petlju napiši funkciju koji određuje koliko godina treba da prođe dok se u
uloženi novac u banku ne udvostruči. Funkcija kao parametar prima kamatnu stopu na godišnjem nivou,
a vraća broj godina.
"""


def broj_godina(kamatna_stopa):
    osnovica = 1000
    trenutno_stanje = osnovica
    brojac = 0
    while trenutno_stanje < 2 * osnovica:
        trenutno_stanje = trenutno_stanje + trenutno_stanje * kamatna_stopa
        brojac += 1

    return brojac


print(broj_godina(0.04))
