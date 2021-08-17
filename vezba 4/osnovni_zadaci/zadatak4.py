'''
Napisati program koji pita korisnika da unese jedan string, potom ispisuje taj string u tri reda. Prvi red
treba da bude ispisan velikim slovima, drugi malim slovima, a u trećem redu trebaju početna slova svake
reči biti velika, a ostala mala.
'''


def main():
    string = input("Unesite string: ")

    print(string.upper())
    print(string.lower())
    print(string.title())


main()
