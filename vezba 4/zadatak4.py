
#Napiši program koji učitava iz tekstulanog fajla korisnička imena i ispisuje ih.




def main():
    f=open("korisnici.txt")
    text = f.readlines()


    for i in text:
        podaci  = text.split("|")
        print("ime", podaci[0])
        print("sifra", podaci[1])

    f.close()



def prikazi_korisnike():
    f = open("korisnici.txt")
    korisnici = f.readlines()

    for korisnik in korisnici:
        korisnicki_podaci = korisnik.strip().split("|")



        print("korisnicko ime: ", korisnicki_podaci[0])
        print("lozinka: ", korisnicki_podaci[1])
    
    f.close()

prikazi_korisnike()

