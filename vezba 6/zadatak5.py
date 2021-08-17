"""
Dadilja naplaćuje 150din po satu čuvanja dece do 9 sati uveče, a 100din po satu čuvanja dece
posle 9 sati uveče. Napiši funkciju koja kao parametre prima vreme kada dadilja počinje da čuva decu i
kada završava učuvanje dece, a vraća poruku o zaradi koja treba da se isplati. Vreme je zadato u formatu
hh:mm, a pretpostavlja se da se čuvanje dece odvija u periodu od 24h.
"""
def dadilja(pocetak, kraj):
    pocetak_split = pocetak.split(":")
    kraj_split = kraj.split(":")

    sati_pocetak = float(pocetak_split[0])
    minuti_pocetak = float(pocetak_split[1])/60
    vreme_pocetak = sati_pocetak + minuti_pocetak
  #  print("pocetak-",vreme_pocetak)

    sati_kraj = float(kraj_split[0])
    minuti_kraj = float(kraj_split[1])/60
    vreme_kraj = sati_kraj + minuti_kraj
   # print("KRAJ- ",vreme_kraj)

    if vreme_pocetak > 21:
        zarada = round((vreme_kraj - vreme_pocetak)*150)
    elif vreme_kraj <= 21:
        zarada = round((vreme_kraj - vreme_pocetak)*100)
    else:
        zarada = round((vreme_kraj - 21) * 100 + (21 - vreme_pocetak)*150)

    return f"Zarada dadilje je: {zarada}rsd."


print(dadilja('20:35', '4:50'))
