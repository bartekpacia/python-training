def find_smallest_index(numbers):
    smallest = numbers[0]
    smallest_index = 0
    for i in range(0, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
            smallest_index = i

    return smallest_index


def selection_sort(numbers):
    sorted_numbers = []

    for i in range(0, len(numbers)):
        smallest_index = find_smallest_index(numbers)
        sorted_numbers.append(numbers[smallest_index])
        numbers.pop(smallest_index)

    return sorted_numbers


if __name__ == "__main__":
    print("Enter numbers. Press Enter to sort them.")

    numbers = []

    while True:
        number = input("Enter number: ")

        if len(str(number)) == 0:
            break
        else:
            numbers.append(int(number))

    numbers = selection_sort(numbers)

    print(numbers)
