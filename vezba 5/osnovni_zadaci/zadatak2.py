"""
Napisati funkciju koja prima dva parametra. Prvi parametar je neki broj n, a drugi parametar je neki tekst.
Funkcija treba da dobijeni tekst ispiše na ekranu n puta.
"""


def ispisi_tekst(n, tekst):
    for i in range(n):
        print(tekst)


ispisi_tekst(10, "Dobro vece! ")
