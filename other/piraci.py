from datetime import date
from datetime import datetime
import datetime
dni = 150

poczatek = date(1902, 10, 1)
wigilia = date(1902, 12, 24)
dzisiaj = poczatek

roznica = wigilia - poczatek
print(roznica)

coords = {"x": 0, "y": 0}
mile_na_polnoc = 0
dystans = 0  # całkowita przebyta odległość
dublony = 0

for dzien in range(1, dni + 1):
    nowe_dublony = 0
    # dodatkowe dublony każdego trzeciego dnia miesiąca
    if dzisiaj.day == 3:  # wychodzi na to, że dni są o jeden zaniżone
        nowe_dublony += 2
        print("Znaleziono dodatkowe 2 dublony!")

    coords["y"] += 8
    coords["x"] += 11
    mile_na_polnoc += 8
    dystans += (8 + 11)

    nowe_dublony += len(str(mile_na_polnoc))

    dublony += nowe_dublony
    coords["x"] -= nowe_dublony
    dystans += nowe_dublony

    print("Dzień " + str(dzien) + " | " + str(dzisiaj))
    print("Przebyty dystans: " + str(dystans) +
          ", na północ: " + str(mile_na_polnoc))
    print("Nowe dublony: " + str(nowe_dublony))
    print("Dublony łącznie: " + str(dublony))
    print("Obóz w x: " + str(coords["x"]) + "  y: " + str(coords["y"]))
    print("- - - - - - - - - - - - - - - -")

    dzisiaj = dzisiaj + datetime.timedelta(1)
