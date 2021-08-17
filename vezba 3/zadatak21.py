'''
Paket math sadrži funkciju za izračunavanje kvadratnog korena. Potrebno je napisati
sopstvenu funkciju za izračunavanje kvadratnog korena pomoću PiP („probaj-i-ponovo“) pristupa. Prvo
pokušamo da pogodimo vrednost korena i uporedimo je sa pravom vrednošću (koju vraća sqrt). Onda
napravimo sledeći pokušaj i približimo se rešenju. Postupak ponavljamo dok ne naiđemo na pravu
vrednost korena ili njenu dovoljno dobru aproksimaciju. Za ovaj posao možemo koristiti Njutnov metod.
Neka je x broj čiji koren tražimo, i guess broj kojim pokušavamo da pogodimo koren. Pokušaj se
može popraviti korišćenjem vrednosti (guess+x/guess)/2 u sledećem krugu. Napiši program koji implementira
Njutnov metod. Program od korisnika traži broj čiji koren tražimo (x) i broj pokušaja. Početna vrednost
za pokušaj je x/2. Na kraju rada ispisati dobijenu vrednost Njutnovom metodom i vrednost koju vraća
sqrt.
'''

from math import sqrt


def main():
    x = eval(input("Unesite x: "))
    n = eval(input("Unesite broj pokusaja: "))
    guess = x/2

    for i in range(n):
        guess = (guess+x/guess)/2

    print("sqrt:", sqrt(x), ", Njutn:", guess)


main()
