"""
Formula za izračunavanje datuma na koji pada uskrs u Gregorijanskom kalendaru data u
prethodnom zadatku važi za sve godine od 1900 do 2099, osim za 1954., 1981., 2049. i 2076. Za te
godine ova formula daje rezultat koji je nedelju dana kasnije nego što treba. Modifikuj zadatak 6 tako da
važi za sve godine od 1900 do 2099.
"""


def uskrs(godina):

    if godina < 1900 or godina > 2099:
        return "godina nije u predvidjenom opsegu"

    a = godina % 19
    b = godina % 4
    c = godina % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7

    datum_uskrsa = 22 + d + e

    if godina in {1954, 1981, 2049, 2076}:
        datum_uskrsa -= 7

    if datum_uskrsa > 31:
        datum_uskrsa -= 31
        return f"Uskrs je {datum_uskrsa}. aprila {godina}. godine"

    return f"Uskrs je {datum_uskrsa}. marta {godina}. godine"


print(uskrs(1981))
