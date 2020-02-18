def count(arr):
    if arr == []:
        return 0
    else:
        new_arr = arr[1:]
        return 1 + count(new_arr)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    print(count(arr))
