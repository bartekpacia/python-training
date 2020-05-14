def napisz(n, symbol):

    if n % 2 == 0:
        return  # działa tylko dla nieparzystych

    podlogi = -1
    for i in range(0, (n * 2) - 1):
        if i / n < 1:
            podlogi += 1
        else:
            podlogi -= 1

        for podloga in range(podlogi):
            print("_", end="")

        print(symbol)


napisz(3, "O")
