'''https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_od_2015/MIN-R2_1P-152.pdf
zadanie 6'''


class Kierowca:
    def __init__(self, id, nazwisko, imie, kraj):
        self.id = id
        self.nazwisko = nazwisko
        self.imie = imie
        self.kraj = kraj

    def __str__(self):
        return "id: " + self.id + " nazwisko: " + self.nazwisko + " imie: " + self.imie + " kraj: " + self.kraj


class Wyscig:
    def __init__(self, id, rok, miejsce):
        self.id = id
        self.rok = rok
        self.miejsce = miejsce

    def __str__(self):
        return "id: " + self.id + " rok: " + self.rok + " miejsce:" + self.miejsce


f = open("Kierowcy.txt", "r")
f.readline()  # pozbycie się nagłówków
line = f.readline()
kierowcy = list()

while line:
    k = line.split(";")  # rozdzielanie danych pojedyńczego kierowcy
    kierowca = Kierowca(k[0], k[1], k[2], k[3])
    kierowcy.append(kierowca)

    line = f.readline()

f.close()
