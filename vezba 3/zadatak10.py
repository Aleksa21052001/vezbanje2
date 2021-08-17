'''
Dve tačke u ravni date su koordinatama (x1; y1) i (x2; y2). Napiši program koji izračunava
nagib prave koja prolazi kroz date tačke
'''

def main():
    x1,y1 = eval(input("(x1,y1):"))
    x2,y2 = eval(input("(x2,y2):"))

    nagib=(y2-y1)/(x2-x1)

    print("Nagib iznosi:" ,nagib)

main()