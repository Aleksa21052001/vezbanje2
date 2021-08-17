'''
Napiši program koji izračunava molekularnu masu molekula ugljovodonika zavisno od broja
atoma ugljenika i vodonika koji ga čine. Mase atoma su sledeće H = 1.0079, C = 12.011.
'''

def main():
    c = 12.011
    h = 1.0079

    broj_c = eval(input("Broj atoma ugljenika: "))
    broj_h = eval(input("Broj atoma vodonika: "))
    masa = c * broj_c + h * broj_h
    print("Molekularna masa je: ", masa)

main()