"""
Datum na koji pada uskrs u Gregorijanskom kalendaru za godine 1982–2048 se računa po formuli:
a=year%19;
b=year%4;
c=yera%7;
d=(19a+24)%30;
e=(2b+4c+6d+5)%7
Datum na koji pada uskrs je 22+d+e mart (ako je vrednost veća od 31 onda je april). Napiši funkciju koja
računa datum uskrsa. Funkcija kao parametar prima godinu i vraća poruku sa informacijom kada je uskrs
ako je godina u zadatom opsegu, odnosno poruku da je došlo do greške ako godina nije u zadatom
opsegu.
Napomena: Postoji greska u primeru izvrsavanja programa!
"""


def uskrs(godina):

    if godina < 1982 or godina > 2048:
        return "godina nije u predvidjenom opsegu"

    a = godina % 19
    b = godina % 4
    c = godina % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7

    datum_uskrsa = 22 + d + e

    if datum_uskrsa > 31:
        datum_uskrsa -= 31
        return f"Uskrs je {datum_uskrsa}. aprila {godina}. godine"

    return f"Uskrs je {datum_uskrsa}. marta {godina}. godine"


print(uskrs(2021))
