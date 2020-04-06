liczby = []
with open("dane/liczby.txt", "r") as file:
    line = file.readline()
    while line:
        line = line.strip()
        liczby.append(int(line))

        line = file.readline()


def oblicz_nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def podzielnosc_przez(dzielnik):
    podzielne = 0

    for liczba in liczby:
        liczba_spr = liczba

        while liczba_spr:

            liczba_spr = liczba_spr / dzielnik

            if liczba_spr == 1:
                podzielne += 1

    return podzielne


def silnia(liczba):
    if liczba == 0 or liczba == 1:
        return 1
    else:
        return liczba * silnia(liczba - 1)


def sprawdz_silnie():
    pasujace_liczby = []
    for liczba in liczby:
        cyfry = [int(x) for x in str(liczba)]

        suma_silni = 0
        for cyfra in cyfry:
            suma_silni += silnia(cyfra)

        if liczba == suma_silni:
            pasujace_liczby.append(liczba)

    return pasujace_liczby


def sprawdz_ciag():
    pierwsza = 0
    dlugosc = 1
    nwd = 1

    # pierwsza liczba, długość, nwd
    tuple_najdluzszy_ciag = (pierwsza, dlugosc, nwd)
    for i in range(1, len(liczby)):
        _nwd = oblicz_nwd(liczby[i], liczby[i - 1])

        if _nwd == nwd and _nwd != 1:
            dlugosc += 1
            tuple_najdluzszy_ciag = (pierwsza, dlugosc, _nwd)
        else:
            pierwsza = liczby[i - 1]
            dlugosc = 3
            nwd = _nwd

        if dlugosc > tuple_najdluzszy_ciag[1]:
            tuple_najdluzszy_ciag = (pierwsza, dlugosc, nwd)

    return tuple_najdluzszy_ciag


print(f"podzielne przez 3: {podzielnosc_przez(3)}")

for pasujace in sprawdz_silnie():
    print(f"silnia == cyfry: {pasujace}")

ciag = sprawdz_ciag()
print(f"ciag: {ciag}")
