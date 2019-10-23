t = int(input("podaj t: "))

wszystkie_liczby = []
for i in range(0, t):
    liczby = input("podaj A B k: ")
    wszystkie_liczby.append(liczby.split())

print(wszystkie_liczby)

for i in range(0, len(wszystkie_liczby)):
    A = wszystkie_liczby[i][0]
    B = wszystkie_liczby[i][1]
    k = int(wszystkie_liczby[i][2])
    print(f"A: {A}, B: {B}, k: {k}")

    najwieksze_dobre_C = 0
    for ii in range(0, k):
        for j in range(0, len(A)):
            for l in range(0, 10):
                C_list = list(A)
                zmieniona_cyfra = str(l)
                C_list[j] = zmieniona_cyfra
                kandydat_C = "".join(C_list)

                if int(kandydat_C) < int(B):
                    if int(kandydat_C) > int(najwieksze_dobre_C):
                        najwieksze_dobre_C = kandydat_C

    print(najwieksze_dobre_C + " - najwieksze dobre")
