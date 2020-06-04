def print_z(size):
    print(("*") * size)

    for i in range(2, size):
        front = size - i - 1
        tail = size - front - 1
        print((" ") * front, end=" ")
        print("*", end=" ")
        print((" ") * tail, end=" ")
        print()

    print(("*") * size)


print_z(7)
