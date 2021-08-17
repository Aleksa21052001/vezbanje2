"""
Napisati funkciju koja prima parametre a,b i c, i vraća rešenja
kvadratne jednačine. Pri tome se predpostavlja da postoje realni koreni kvadratne jednačine.
"""


def kvadratna_jednacina(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

    return x1, x2


print(kvadratna_jednacina(-1, 5, 5))
