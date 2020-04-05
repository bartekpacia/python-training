n = int(input())

banknotes = 0
n = n
while n > 0:
    if n >= 100:
        n -= 100
    elif n >= 20:
        n -= 20
    elif n >= 10:
        n -= 10
    elif n >= 5:
        n -= 5
    elif n >= 1:
        n -= 1

    banknotes += 1

print(banknotes)
