'''
Za dve tačke u ravni (vidi prethodni zadatak) izračunati rastojanje između nj
'''

from math import sqrt

def main():
    x1, y1 = eval(input("(x1,y1):"))
    x2, y2 = eval(input("(x2,y2):"))

    rastojanje = sqrt((x2-x1)**2 + (y2-y1)**2)

    print("Rastojanje izmedju dve tacke je: " , rastojanje)

main()