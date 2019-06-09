file = open("olaimati.txt", "w")

for number in range(0, 10_000_000):
    file.write("Ola i Mati śmierdzą do potęgi " + str(number) + "\n")

file.close()