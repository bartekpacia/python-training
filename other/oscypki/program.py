from datetime import date, timedelta

liczba_owiec = 600
poczatek = date(2014, 4, 23)
koniec = date(2014, 9, 29)
dni = (koniec - poczatek).days + 1  # bo ostatni element range() jest wyłączny
dawane_mleko = 0.5
dzien_sezonu = 1

cale_mleko = 0

print(f"Dni: {dni}")

for dzien in (poczatek + timedelta(n) for n in range(dni)):
    print(f"{dzien}, {dzien_sezonu} dzień sezonu")

    mleko_dzis = 0

    if dzien <= date(2014, 4, 29):
        mleko_dzis = 0.5

    elif dzien <= date(2014, 6, 24):
        if dzien_sezonu % 7 == 1:  # czy zaczął się już nowy tydzień?
            dawane_mleko = round(dawane_mleko * 1.04, 2)

    else:
        if dzien_sezonu % 7 == 1:
            dawane_mleko = round(dawane_mleko * 0.9, 2)

    print(f"Mleko od jednej owcy: {dawane_mleko}")

    cale_mleko += dawane_mleko * liczba_owiec

    dzien_sezonu += 1

print(f"Całe mleko: {cale_mleko}")
