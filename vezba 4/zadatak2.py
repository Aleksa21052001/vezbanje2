"""
Napiši program koji formira akronim za zadatu frazu. Akronim se sastoji od kapitalizovanih
prvih slova reči u frazi. Na primer RAM je akronim za frazu „random access memory“.
"""


def main():
    fraza = input("Unesite frazu: ")
    reci = fraza.split(" ")

    akronim = ""
    for rec in reci:
        akronim += rec[0].upper()

    print("Akronim za unetu frazu je: ", akronim)


main()
