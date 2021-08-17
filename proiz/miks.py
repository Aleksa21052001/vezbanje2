# Napisati funkciju koja kao parametar prima putanju do datoteke u kojoj pišu visina, širina i naziv prozora.
# Funkcija treba da pročita podatke iz datoteke i vrati prozor kreiran sa tim podacima. Primer sadržaja datoteke: 500,500,moj_novi_prozor

import turtle

def main(datoteka):
    f = open(datoteka)

    podaci = f.read()
    print(podaci)

    f.close()

    lista_podataka = podaci.split(",")

    screen = turtle.Screen()

    visina = int(lista_podataka[0])
    sirina = int(lista_podataka[1])
    title = lista_podataka[2]


    screen.setup(visina,sirina)
    screen.title(title)

    screen.exitonclick()


prozor = main("kon.txt")
