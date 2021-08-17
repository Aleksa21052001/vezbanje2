"""
Napisati program koji traži od korisnika da unese broj n. Program potom sabira prirodne brojeve redom od
1 pa na dalje, sve dok zbir ne postane veći od broja n. Kada zbir postane veći od n, program ispiše koliko je
brojeva sabrao, i koliki je zbir.
"""





def main():
    n = int(input("n: "))
    zbir = 0
    brojac = 0

    while zbir <= n:
        brojac += 1
        zbir += brojac

    print("Zbir je", zbir, "a sabrano je", brojac, "brojeva")

main()

