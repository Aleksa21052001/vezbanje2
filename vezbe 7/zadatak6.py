"""
Najveći zajednički delilac se računa pomoću Euklidovog algoritma: za brojeve m i n se
ponavlja n_(i+1)=mi, m_(i+1)=n_i%m_i dok m ne stigne do 0. Kada m postane 0, n je naveći zajednički delilac. Napiši
funkciju koja implementira Euklidov algoritam za računanje najvećeg zajedničkog delioca. Funkcija prima
dva prirodna broja, a vraća njihov najveći zajednički delilac.
"""


def nzd(n, m):

    while m != 0:
        n_old = n
        n = m
        m = n_old % m

    return n


print(nzd(25, 5))
