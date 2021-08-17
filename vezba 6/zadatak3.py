"""
Indeks telesne mase se računa po sledećoj formuli BMI=m/h^2 u kojoj je m masa u
kilogramima, a h visina u metrima. U tabeli je data preporučena klasifikacija indeksa telesne mase:

BMI         Klasifikacija
------------------------------------
<18,5       Pothranjenost
18,5 - 25   Idealna telesna težina
25 - 30     Preterana telesna težina
>30         Gojaznost
------------------------------------
"""


def indeks_telesne_mase(tezina, visina):
    bmi = float(tezina)/float(visina**2)

    if bmi < 18.5:
        print("pothranjenost")
    elif bmi >= 18.5 and bmi < 25:
        print("idealna telesna težina")
    elif bmi >= 25 and bmi <= 30:
        print("preterana telesna težina")
    elif bmi > 30:
        print("gojaznost")


indeks_telesne_mase(84, 1.7)
