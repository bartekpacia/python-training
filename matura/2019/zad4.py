liczby = []
with open("dane/liczby.txt", "r") as file:
    line = file.readline()
    while line:
        print(repr(line))
        liczby.append(int(line))

        line = file.readline()
