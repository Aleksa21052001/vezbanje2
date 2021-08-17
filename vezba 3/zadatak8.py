'''
Napiši program koji određuje udaljenost posmatrača od munje na bazi vremenske razlike
trenutka pojavljivanja munje i trenutka kada zvuk stigne do posmatrača. Brzina zvuka iznosi 340 m/s.
'''

def main():
    vremenski_interval = eval(input("Unesite vremensku razlika t: "))
    brzina_zvuka = 340
    distanca = brzina_zvuka * vremenski_interval

    print("Rastojanje munje i posmatraca je: ", distanca)

main()