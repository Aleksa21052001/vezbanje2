"""
Napiši program koji od korisnika traži da unese dva stringa i formira i ispisuje novi string koji
se sastoji od dva puta ponovljena prva tri karaktera iz prvog stringa i poslednja tri karaktera prethodnog
stringa.
"""


def main():
    prvi_string = input("Unesite prvi string: ")
    drugi_string = input("Unesite drugi string: ")

    print(2 * prvi_string[:3] + drugi_string[-3:])


main()
