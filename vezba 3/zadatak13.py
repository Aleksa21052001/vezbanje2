'''
Napiši program koji izračunava površinu trougla za date dužine stranica a, b i c.
'''
from math import sqrt


def main():
    a,b,c = eval(input("a,b,c: "))
    s=(a+b+c)/2
    A=sqrt(s*(s-a)*(s-b)*(s-c))
    print("Povrsina trougla iznosi: ", A)


main()
