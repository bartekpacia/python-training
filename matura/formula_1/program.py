# -*- coding: utf-8 -*-

# https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_od_2015/MIN-R2_1P-152.pdf zadanie 6'''

# https://cke.gov.pl/egzamin-maturalny/egzamin-w-nowej-formule/arkusze/2015-2

import operator
from klasy import Kierowca, Wyscig, Wynik
kierowcy = []
wyscigi = []
wyniki = []

with open("Kierowcy.txt") as f:
    f.readline()  # pozbycie się nagłówków
    line = f.readline()

    while line:
        k = line.split(";")  # rozdzielanie danych pojedyńczego kierowcy
        kierowca = Kierowca(k[0], k[1], k[2], k[3])
        kierowcy.append(kierowca)

        line = f.readline()

with open("Wyscigi.txt") as f:
    f.readline()
    line = f.readline()

    while line:
        line = line.strip()

        wynik = line.split(";")
        wyscig = Wyscig(wynik[0], int(wynik[1]), wynik[2])
        wyscigi.append(wyscig)

        line = f.readline()

with open("Wyniki.txt") as f:
    f.readline()  # pozbycie się nagłówków
    line = f.readline()

    while line:
        line = line.strip()  # Pozbycie się znaków nowych linii  \n

        wynik = line.split(";")  # rozdzielanie danych pojedyńczego kierowcy
        punkty = float(wynik[1].replace(",", "."))
        wynik = Wynik(wynik[0], punkty, wynik[2])
        wyniki.append(wynik)

        line = f.readline()

print("Dane załadowane pomyślnie")

# zadanie 6.1

id_roberta = list(filter(lambda k: k.nazwisko == "Kubica", kierowcy))[0].id
max_punkty = 0
id_najlepszego_wyscigu = None
najlepszy_wyscig = None

for wynik in wyniki:
    if wynik.id_kierowcy == id_roberta:
        if wynik.punkty > max_punkty:
            max_punkty = wynik.punkty
            id_najlepszego_wyscigu = wynik.id_wyscigu

najlepszy_wyscig = list(
    filter(lambda wyscig: wyscig.id == id_najlepszego_wyscigu, wyscigi))[0]


print("Najlepszy wyścig Roberta: " + str(najlepszy_wyscig))

# zadanie 6.2
wyscigi_nowe = []
kraje = {}

for wyscig in wyscigi:
    if wyscig.rok >= 2002 and wyscig.rok <= 2012:
        wyscigi_nowe.append(wyscig)

        kraj = wyscig.miejsce
        if kraj not in kraje:
            kraje[kraj] = 1
        else:
            kraje[kraj] += 1


najmniej_razy = min(kraje.values())
najmniej_popularne_miejsca = {key: value for (
    key, value) in kraje.items() if value == najmniej_razy}


print(najmniej_popularne_miejsca)
