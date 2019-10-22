t = int(input("podaj t: "))

wszystkie_liczby = []
for i in range(0, t):
    liczby = input("podaj A B k: ")
    wszystkie_liczby.append(liczby.split())

print(wszystkie_liczby)

# narazie implementuję to tylko dla k = 1

for i in range(0, len(wszystkie_liczby)):
    A = wszystkie_liczby[i][0]
    B = wszystkie_liczby[i][1]
    k = int(wszystkie_liczby[i][2])
    print(f"A: {A}, B: {B}, k: {k}")

    for j in range(1, len(A) + 1):
        for k in range(0, 10):
            nowe_A = str(str(k) + A[j:])
            print(nowe_A)
