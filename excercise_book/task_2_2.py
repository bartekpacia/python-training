import math as Math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# ax^2 + bx + c = 0

if a == 0:
    print("a can't be 0")
else:
    # delta = b^2 - 4 * a * c
    delta = b * b - 4 * a * c
    print("Delta: " + str(delta))

    if(delta >= 0):
        x1 = (-b - Math.sqrt(delta)) / (2 * a)
        x2 = (-b + Math.sqrt(delta)) / (2 * a)

        rounded_x1 = round(x1, 2)
        rounded_x2 = round(x2, 2)

        print("x1:" + str(rounded_x1))
        print("x2:" + str(rounded_x2))
    else: 
        print("delta < 0")