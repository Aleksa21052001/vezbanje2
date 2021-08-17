"""
Napisati program koji traži od korisnika da unese neko ime. Ukoliko korisnik unese Boban, program treba da
ispiše Zdravo Bobane!. Ukoliko je korisnik uneo Milivoje, program treba da ispiše Cao Milivoje!. Ukoliko
je korisnik uneo neko drugo ime, program ispisuje Ja ne znam ko si ti :(.
"""


def main():
    ime = input("unesite ime: ")

    if ime == "Boban":
        print("Zdravo Bobane!")
    elif ime == "Milivoje":
        print("Cao Milivoje!")
    else:
        print("Ja ne znam ko si ti :(")


main()
