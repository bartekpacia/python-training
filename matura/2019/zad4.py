mapy = []
rozmiar = 30

file = open("dane/dzialki.txt", "r")

# dla każdej z 50 działek
for i in range(1):
    mapa = [[0 for x in range(rozmiar)] for y in range(rozmiar)]
    # dla każdej z 30 linijek w 1 działce
    for i in range(rozmiar):
        linia = file.readline().strip("\n")
        # dla każdego z 30 pól w 1 linijce
        for j, znak in enumerate(linia):
            mapa[i][j] = znak

    mapy.append(mapa)
    file.readline()


print(mapy[0])

file.close()
