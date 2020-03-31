arr = [1, 2]
s = "yes"


def change(_arr, _s):
    _arr.append(3)
    _s = "no"


change(arr, s)
print(f"arr: {arr}, s: {s}")
