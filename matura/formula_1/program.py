# -*- coding: utf-8 -*-

# https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_od_2015/MIN-R2_1P-152.pdf zadanie 6'''

# https://cke.gov.pl/egzamin-maturalny/egzamin-w-nowej-formule/arkusze/2015-2

import operator
from klasy import Kierowca, Wyscig, Wynik
kierowcy = []
wyscigi = []
wyniki = []

plik_z_wynikami = "wynik6.txt"

with open("dane/Kierowcy.txt") as f:
    f.readline()  # pozbycie się nagłówków
    line = f.readline()

    while line:
        line = line.strip()

        k = line.split(";")  # rozdzielanie danych pojedyńczego kierowcy
        kierowca = Kierowca(k[0], k[1], k[2], k[3])
        kierowcy.append(kierowca)

        line = f.readline()

with open("dane/Wyscigi.txt") as f:
    f.readline()
    line = f.readline()

    while line:
        line = line.strip()

        wynik = line.split(";")
        wyscig = Wyscig(wynik[0], int(wynik[1]), wynik[2])
        wyscigi.append(wyscig)

        line = f.readline()

with open("dane/Wyniki.txt") as f:
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

f = open(plik_z_wynikami, "w+")
print("Najlepszy wyścig Roberta: " + str(najlepszy_wyscig))
f.write("Najlepszy wyścig Roberta: " + str(najlepszy_wyscig) + "\n")

# zadanie 6.2
wyscigi_nowe = []
kraje = {}

for wyscig in wyscigi:
    if wyscig.rok >= 2000 and wyscig.rok <= 2012:
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
f.write("Najmniejszą liczbę wyścigów Grand Prix w latach 2000-2012 rozegrano w " +
        str(list(najmniej_popularne_miejsca)) + "\n")

# zadanie 6.3
kierowcy_i_punkty = {}


def wez_kierowce(id_kierowcy):
    for kierowca in kierowcy:
        if id_kierowcy == kierowca.id:
            return kierowca


def zrob_klasyfikacje(rok):
    wyscigi_w_roku = []
    for wyscig in wyscigi:
        if wyscig.rok == rok:
            wyscigi_w_roku.append(wyscig)

    # for w in wyscigi_w_roku:
    #    print(w)

    wyniki_w_roku = []
    for wynik in wyniki:
        for wyscig in wyscigi_w_roku:
            if wynik.id_wyscigu == wyscig.id:
                wyniki_w_roku.append(wynik)

    klasyfikacja = {}  # id_kierowcy : punkty
    for wynik in wyniki_w_roku:
        if wynik.id_kierowcy not in klasyfikacja:
            klasyfikacja[wynik.id_kierowcy] = wynik.punkty
        else:
            klasyfikacja[wynik.id_kierowcy] += wynik.punkty

    # zamiana id_kierowcy na imię i nazwisko
    for id_kierowcy, punkty in set(klasyfikacja.items()):
        kierowca = wez_kierowce(id_kierowcy)
        imie_nazwisko = kierowca.imie + " " + kierowca.nazwisko
        klasyfikacja[imie_nazwisko] = klasyfikacja.pop(id_kierowcy)

    klasyfikacja_list_sort = sorted(
        klasyfikacja, key=klasyfikacja.get, reverse=True)

    # for key in klasyfikacja_list_sort:
    #    print(key, klasyfikacja[key])

    lider = klasyfikacja_list_sort[0]  # pierwszy ma najwięcej punktów
    punkty_lidera = klasyfikacja[lider]

    f.write("Sezon: " + str(rok) + ", Lider: " +
            lider + ", Suma punktów: " + str(punkty_lidera) + "\n")


zrob_klasyfikacje(2000)
zrob_klasyfikacje(2006)
zrob_klasyfikacje(2012)

# zadanie 6.4

kierowcy_w_2012 = []

for wyscig in wyscigi:
    if wyscig.rok == 2012:
        for wynik in wyniki:
            if wynik.id_wyscigu == wyscig.id:
                kierowca = wez_kierowce(wynik.id_kierowcy)
                kierowcy_w_2012.append(kierowca)

kierowcy_w_2012 = list(dict.fromkeys(kierowcy_w_2012))

kraje = {}  # kraj: liczba

for kierowca in kierowcy_w_2012:
    kraje[kierowca.kraj] = 0


for a in kierowcy_w_2012:
    print(a)

for kraj, liczba in kraje.items():
    for kierowca in kierowcy_w_2012:
        if kierowca.kraj == kraj:
            kraje[kraj] += 1

f.write("Zestawienie liczby zawodników reprezentujących swój kraj w 2012 roku\n")
for kraj, liczba in kraje.items():
    print(kraj, liczba)
    f.write(kraj + ": " + str(liczba) + "\n")

f.close()
