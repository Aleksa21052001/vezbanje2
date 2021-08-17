"""
Napiši funkciju koji obračunava zaradu radnika. Radnici koji rade više od 40 sati nedeljno su
plaćeni 1.5 puta više nego što bi bili plaćeni da rade do 40 sati nedeljno. Broj radnih sati po danima
završene radne nedelje se učitava iz fajla. Funkcija kao parametar prima putanju do fajla sa radnim
satima i cenu radnog sata i ispisuje imena i zarade radnika.

"""
def obracun(putanja, satnica):
    f = open(putanja, "r")
    redovi = f.readlines()

    for red in redovi:
        lista_radnika = red.strip().split("|")

        suma_sati = 0
        for i in range(1, len(lista_radnika)):
            suma_sati= suma_sati + int(lista_radnika[i])

        zarada = suma_sati*satnica

        if suma_sati > 40:
            zarada = zarada*1.5

        print(lista_radnika[0] +":", zarada)


obracun('radnici.txt', 400)



def izracunaj_zaradu(datoteka, satnica):
    f = open(datoteka)
    redovi = f.readlines()

    for red in redovi:
        radnik = red.strip().split('|')
        broj_sati = 0

        for i in range(1, len(radnik)):
            broj_sati = broj_sati + int(radnik[i])

        zarada = broj_sati * satnica

        if broj_sati > 40:
            zarada = zarada * 1.5

        print("ime:", radnik[0])
        print("zarada:", zarada)



