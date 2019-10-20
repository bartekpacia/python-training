'''https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_od_2015/MIN-R2_1P-152.pdf
zadanie 6'''


class Kierowca:
    def __init__(self, id, nazwisko, imie, kraj):
        self.id = id
        self.nazwisko = nazwisko
        self.imie = imie
        self.kraj = kraj

    def __str__(self):
        return "Kierowca id: " + self.id + ", nazwisko: " + self.nazwisko + ", imie: " + self.imie + ", kraj: " + self.kraj


class Wyscig:
    def __init__(self, id, rok, miejsce):
        self.id = id
        self.rok = rok
        self.miejsce = miejsce

    def __str__(self):
        return "Wyscig id: " + self.id + ", rok: " + self.rok + ", miejsce: " + self.miejsce


class Wynik:
    def __init__(self, id_kierowcy, punkty, id_wyscigu):
        self.id_kierowcy = id_kierowcy
        self.punkty = punkty
        self.id_wyscigu = id_wyscigu

    def __str__(self):
        return "Wynik id_kierowcy: " + self.id_kierowcy + ", punkty: " + str(self.punkty) + ", id_wyscigu:" + self.id_wyscigu


kierowcy = list()
wyscigi = list()
wyniki = list()

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
        wynik = line.split(";")
        wyscig = Wyscig(wynik[0], wynik[1], wynik[2])
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

id_roberta = list(filter(lambda k: k.nazwisko == "Kubica", kierowcy))[0].id

print("id_roberta: " + id_roberta)
wyniki_roberta = list()
max_punkty = 0
id_najlepszego_wyscigu = None
najlepszy_wyscig = None

for wynik in wyniki:
    if wynik.id_kierowcy == id_roberta:
        if wynik.punkty > max_punkty:
            max_punkty = wynik.punkty
            id_najlepszego_wyscigu = wynik.id_wyscigu

print("id_najlepszego_wyscigu: " + id_najlepszego_wyscigu)

najlepszy_wyscig = list(
    filter(lambda wyscig: wyscig.id == id_najlepszego_wyscigu, wyscigi))[0]

print("Najlepszy wyścig Roberta: " + str(najlepszy_wyscig))
