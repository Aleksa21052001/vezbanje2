"""
Subjektivni osećaj hladnoće se računa po formuli:

3.74+0.6215T-35.75(V^0.16)+0.4275T(V^0.16)

gde je T temperatura u stepenima Farenhajta, a V brzina vetra u miljama na sat. Napiši program koji
ispisuje tabelu subjektivnog osećaja hladnoće za interval temperature i brzine vetra koje unosi korisnik.
"""

def tabela(min_v, max_v, min_t, max_t):

    zaglavlje = "\t\t"

    for t in range(min_t, max_t + 1):
        vrednost = f"t={t}"
        zaglavlje = zaglavlje + f"{vrednost:<12}" # na zaglavlju(dva taba) dodajemo vrednosti
        #print("\t\t t={:<1}".format(t),end="\t")
    print(zaglavlje)


    for v in range(min_v, max_v + 1):
        print("v={:<5}".format(v),end="") #nema string za novi red
        for t in range(min_t, max_t + 1):
            subjektivni_osecaj = 3.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)
            so = "{:<10.3f}".format(subjektivni_osecaj)
            print(so,end="\t") #da ne ide za svaku vrednost u novi red vec ima razmak
        print() # da na kraju  druge for petlje dodamo znak za novi red


tabela(0,10,5,10)




def napravi_tabelu(min_v, max_v, min_t, max_t):
    zaglavlje = " "*7

    for t in range(min_t, max_t + 1):
        vrednost = f"t={t}"
        zaglavlje = zaglavlje + f"{vrednost:<10}"

    print(zaglavlje)

    for v in range(min_v, max_v + 1):
        print(f"v={v:<5}", end="")

        for t in range(min_t, max_t + 1):
            subjektivni_osecaj = 3.74 + 0.6215 * t - 35.75*(v**0.16) + 0.4275 * t * (v**0.16)

            za_ispis = f"{subjektivni_osecaj:<10.3f}"
            print(za_ispis, end="")
        print()



