'''
Napiši program koji izračunava zapreminu i površinu sfere za dati poluprečnik.
'''

from math import pi

def main():
    r = eval(input("Unesite r: "))

    zapremina = (4/3) * pi * r**3
    povrsina = 4 * pi * r**2

    print("Zapremina sfere:", zapremina)
    print("Povrsina sfere:", povrsina)

main()