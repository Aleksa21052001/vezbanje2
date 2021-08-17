"""
Napisati program koji traži od korisnika da unese neki broj. Program ponavlja pitanje u krug dok korisnik ne
unese broj 42.
"""


def main():
    while True:
        broj = int(input("unesite broj: "))

        if broj == 42:
            break
main()


