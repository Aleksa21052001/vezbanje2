'''
Prodavnica kafe prodaje kafu za 105 dinara za kilogram. Za kućnu dostavu naplaćuje se
18 dinara po kilogramu i 15 dinara fiksnih troškova. Napiši program koji izraćunava ukupnu cenu kućne
porudžbine.
'''
def main():
    narucena_kolicina = eval(input("Unesite koliko kg kafe je naruceno: "))
    cena = narucena_kolicina * (105 + 18) + 15
    print("Ukupna cena kucne porudzbine je:", cena)

main()