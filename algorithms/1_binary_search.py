# Actual implementation of Binary Search algorithm
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:  # Found the element!
            return mid

        if guess > item:
            high = mid - 1

        elif guess < item:
            low = mid + 1

        else:
            return None


if __name__ == "__main__":
    print("Enter numbers. Press Enter to sort them.")

    numbers = []

    while True:
        number = input("Enter number: ")

        if len(str(number)) == 0:
            break
        else:
            numbers.append(int(number))

    numbers.sort()

    looking_for = int(input("What number are you looking for? "))

    print(
        f'Number {looking_for} is at index {binary_search(numbers, looking_for)}')
