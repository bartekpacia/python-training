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
        return "Wyscig id: " + self.id + ", rok: " + self.rok + ", miejsce:" + self.miejsce


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
        w = line.split(";")
        wyscig = Wyscig(w[0], w[1], w[2])
        wyscigi.append(wyscig)

        line = f.readline()

with open("Wyniki.txt") as f:
    f.readline()  # pozbycie się nagłówków
    line = f.readline()

    while line:
        w = line.split(";")  # rozdzielanie danych pojedyńczego kierowcy
        punkty = float(w[1].replace(",", "."))
        wynik = Wynik(w[0], punkty, w[2])
        wyniki.append(wynik)

        line = f.readline()

print(kierowcy[1])
print(wyscigi[1])
print(wyniki[1])


''' Dane Gotowe '''

id_roberta = None
wyniki_roberta = list()
max_punkty = 0
id_najlepszego_wyscigu = None
najlepszy_wyscig = None

for k in kierowcy:
    if k.nazwisko == "Kubica":
        id_roberta = k.id

for w in wyniki:
    if w.id_kierowcy == id_roberta:
        if w.punkty > max_punkty:
            max_punkty = w.punkty
            id_najlepszego_wyscigu = w.id_wyscigu

print("best_wyscig_roberta: " + id_najlepszego_wyscigu)

kubica = list(filter(lambda x: (x.id == id_roberta), kierowcy))
for k in kubica:
    print(str(k))

for wyscig in wyscigi:
    if wyscig.id == id_najlepszego_wyscigu:
        najlepszy_wyscig = wyscig
        print("jest")

print(str(najlepszy_wyscig))
