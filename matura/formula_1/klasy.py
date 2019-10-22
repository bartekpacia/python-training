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
        return "Wyscig id: " + self.id + ", rok: " + str(self.rok) + ", miejsce: " + self.miejsce


class Wynik:
    def __init__(self, id_kierowcy, punkty, id_wyscigu):
        self.id_kierowcy = id_kierowcy
        self.punkty = punkty
        self.id_wyscigu = id_wyscigu

    def __str__(self):
        return "Wynik id_kierowcy: " + self.id_kierowcy + ", punkty: " + str(self.punkty) + ", id_wyscigu:" + self.id_wyscigu
