'''
Napiši program koji izračunava cenu pice po kvadratnom centimetru za dati poluprečnik i
cenu cele pice.
'''
from math import pi

def main():
    r = eval(input("Unesite r: "))
    cena_pice = eval(input("Unesite cenu cele pice: "))
    povrsina_pice = pi * r**2
    cena = cena_pice/povrsina_pice
    print("Cena pice po kvadratnom centimetru je: ", cena)

main()