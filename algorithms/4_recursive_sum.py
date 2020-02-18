def sum(arr: list):
    if len(arr) == 0:
        return 0
    else:
        new_arr = arr[1:]

        print(f"arr = {arr}")
        print(f"len[arr] = {len(arr)}")
        print(f"arr[0] = {arr[0]}")
        print(f"new_arr = {new_arr}")
        print("----")

        return arr[0] + sum(new_arr)


if __name__ == "__main__":
    print("hi")

    arr = [1, 2, 3, 4, 5, 6]
    print(sum(arr))
