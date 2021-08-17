'''
Fibonačijev niz brojeva je niz kod koga svaki broj predstavlja zbir prethodna dva. Ovaj
niz počinje sa 1, 1, 2, 3, 5, 8, 13, ... Napiši program koji izračunava n-ti Fibonačijev broj gde n unosi
korisnik. Fibonačijevi brojevi rastu vrlo brzo, program mora da rukuje vrlo velikim brojevima.
'''


def main():
    n = eval(input("Unesite n: "))
    fib1=1
    fib2=1

    for i in range(3, n+1):
        temp = fib1 + fib2
        fib1 = fib2
        fib2 = temp

    print("Fibonacijev broj je: ", fib2)


main()
