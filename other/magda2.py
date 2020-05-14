from random import randrange


def wygeneruj():
    wygenerowane = []
    for i in range(50):
        losowa = randrange(1, 101)
        wygenerowane.append(losowa)

    slownik = {}
    for klucz in range(1, 11):
        podzielne = []
        for liczba in wygenerowane:
            if liczba % klucz == 0:
                podzielne.append(liczba)

        slownik[klucz] = podzielne

    print(slownik)


wygeneruj()
