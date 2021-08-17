''''
Epakt predstavlja starost meseca u danima na dan 1. januara. Koristi se za izračunavanje
termina Uskrsa. Gregorijanski epakt se izračunava po sledećim formulama (int aritmetika).
'''

def main():
    godina = int(input("Unesite godinu: "))
    c = godina//100
    epakt = (8 + c//4-c+((8*c+13)//25)+11*(godina%19)) % 30
    print("Epakt po Gregorijanskom kalendaru je:", epakt)

main()