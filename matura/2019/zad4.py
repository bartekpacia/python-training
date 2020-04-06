from pprint import pprint
mapy = []
rozmiar = 30


def obroc_180(mapa):
    return [list(a) for a in zip(*mapa[::-1])]


def analizuj_mape_obrot(mapa1, mapa2):
    """
    zwraca True jeśli mapa2 po obróceniu o 180 == mapa1
    w przeciwnym razie False
    """
    if obroc_180(mapa1) == mapa2:
        return True
    else:
        return False


def analizuj_mape_trawa(mapa):
    """
    zwraca procent porośnięcia trawą w stosunku do całej powierzchni
    """
    trawa = 0
    for i in range(rozmiar):
        for j in range(rozmiar):
            if mapa[i][j] == "*":
                trawa += 1

    return trawa / (rozmiar**2)


with open("dane/dzialki.txt", "r") as plik:
    # dla każdej z 50 działek
    for i in range(50):
        mapa = [[0 for x in range(rozmiar)] for y in range(rozmiar)]
        # dla każdej z 30 linijek w 1 działce
        for i in range(rozmiar):
            linia = plik.readline().strip("\n")
            # dla każdego z 30 pól w 1 linijce
            for j, znak in enumerate(linia):
                mapa[i][j] = znak

        mapy.append(mapa)
        plik.readline()


trawiaste = 0
for mapa in mapy:
    ile_trawy = analizuj_mape_trawa(mapa)

    if ile_trawy >= 0.7:
        trawiaste += 1

takie_same_180 = 0
pary_map = []
pary_indeksy_map = []
for index1, mapa1 in enumerate(mapy):
    for index2, mapa2 in enumerate(mapy):
        if analizuj_mape_obrot(mapa1, mapa2) and sorted((index1, index2)) not in pary_map:
            pary_map.append(sorted((mapa1, mapa2)))
            takie_same_180 += 1

print(f"wszystkie mapy: {len(mapy)}")
print(f"z trawą powyżej 0.7: {trawiaste}")
print(f"takie same mapy po obrocie o 180: {pary_map}")
