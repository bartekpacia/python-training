def zamien(s):
    lista = []
    for item in slownik.items():
        lista.append(item)

    return lista


slownik = {"imie": "Magda", "imie": "Andrzej"}

print(zamien(slownik))
