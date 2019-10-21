from datetime import date
dni = 150

poczatek = date(1902, 10, 1)
wigilia = date(1902, 12, 24)

roznica = wigilia - poczatek
print(roznica)

coords = {"x": 0, "y": 0}
mile_na_polnoc = 0
dystans = 0  # całkowita przebyta odległość
dublony = 0

for dzien in range(1, dni + 1):
    coords["x"] += 8
    coords["y"] += 11
    mile_na_polnoc += 8
    dystans += (8 + 11)

    wykopane_dublony = len(str(mile_na_polnoc))

    dublony += wykopane_dublony
    coords["x"] -= wykopane_dublony
    dystans += wykopane_dublony

    print("- - - - - - - - - - - - - - - -")
    print("Dzień " + str(dzien))
    print("Przebyty dystans: " + str(dystans))
    print("Nowe dublony: " + str(wykopane_dublony))
    print("Dublony łącznie: " + str(dublony))
    print("Obóz w x: " + str(coords["x"]) + "  y: " + str(coords["y"]))
