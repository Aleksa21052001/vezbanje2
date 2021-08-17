"""
Zadatak 1. Knjiga koja je opisana identifikatorom, naslovom, autorima, izdavačem, jediničnom cenom,
raspoloživa količina i godinom izdanja. Pri tome ne mogu postojati dve knjige sa identičnim
identifikatorom. Jedan knjiga je predstavljena rečnikom, pri čemu stavke iz opisa knjige odgovaraju
ključevima iz rečnika. Spisak knjiga se je smešten u listu rečnika. Napisati program koji omogućuje
dodavanje nove knjige i pregled svih knjiga iz liste.
Ispis knjiga treba da bude formatiran kao što je prikazano ispod:
"""
def ucitaj_knjige():

    f =  open('knjige.txt')
    redovi = f.readlines()

    knjige = []

    for red in redovi:
        podaci_o_knjizi = red.strip().split('|')

        knjiga = {}

        knjiga["id"] = podaci_o_knjizi[0]
        knjiga["naslov"] = podaci_o_knjizi[1]
        knjiga["autor"] = podaci_o_knjizi[2]
        knjiga["izdavac"] = podaci_o_knjizi[3]
        knjiga["cena"] = podaci_o_knjizi[4]
        knjiga["kolicina"] = podaci_o_knjizi[5]
        knjiga["godina izdanja"] = podaci_o_knjizi[6]

        knjige.append(knjiga)

    f.close()
    return  knjige

def sacuvaj_knjige(spisak_knjiga):

    f = open('knjige.txt','w')

    for knjiga in spisak_knjiga:
        ispis = f"{knjiga['id']}|" \
                f"{knjiga['naslov']}|" \
                f"{knjiga['autor']}|" \
                f"{knjiga['izdavac']}|" \
                f"{knjiga['cena']}|" \
                f"{knjiga['kolicina']}|" \
                f"{knjiga['godina izdanja']}\n"

        f.write(ispis)

    f.close

def pronadji_knjigu(spisak_knjiga ,id):

    for knjiga in spisak_knjiga:
        if knjiga['id'] == id:
            return knjiga


def dodavanje_knjige(spisak_knjiga):

    knjiga = {}

    id = input("unesite id: ")
    naslov = input("naslov: ")
    autor = input("autor: ")
    izdavac = input("izdavac: ")
    cena = input("cena: ")
    raspoloživa_količina = input("kolicina: ")
    godina_izdanja = input("godina izdanja: ")

    knjiga["id"] = id
    knjiga["naslov"] = naslov
    knjiga["autor"] = autor
    knjiga["izdavac"] = izdavac
    knjiga["cena"] = cena
    knjiga["kolicina"] = raspoloživa_količina
    knjiga["godina izdanja"] = godina_izdanja

    if pronadji_knjigu(spisak_knjiga, knjiga['id']) is None:
        spisak_knjiga.append(knjiga)
        #sacuvaj_knjige(spisak_knjiga)
    else:
        print('knjiga sa unetim id vec postoji')



def pregled_knjiga(spisak_knjiga):

    zaglavlje = "{:^10} {:^20} {:^20} {:^20} {:^20} {:^20} {:^20}".format("id", "naslov", "autor", "izdavac", "cena","kolicina", "godina")
    print(zaglavlje)
    print("-"*len(zaglavlje))

    for knjiga in spisak_knjiga:
        ispis = f"{knjiga['id']:^10}{knjiga['naslov']:^20}{knjiga['autor']:^20}{knjiga['izdavac']:^23}{knjiga['cena']:^20}{knjiga['kolicina']:^20}{knjiga['godina izdanja']:^20}"
        print(ispis)
    print("-"*len(zaglavlje))

def main():

    spisak_knjiga = ucitaj_knjige()
    while True:
        print("1. dodavanje nove knjige: ")
        print("2. pregled svih knjiga iz liste: ")
        print("3. kraj")
        x = int(input("izaberite opciju: "))
        if x == 1:
            dodavanje_knjige(spisak_knjiga)
            #sacuvaj_knjige(spisak_knjiga)
        elif x == 2:
            pregled_knjiga(spisak_knjiga)
        elif x == 3:
            sacuvaj_knjige(spisak_knjiga)
            return
        else:
            print("pogresna opcija")

main()