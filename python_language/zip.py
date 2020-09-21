arr1 = [1, 2, 3, 4]
arr2 = [
    "one",
    "two",
    "three",
]

zip_obj = zip(arr1, arr2)

# converting iterator to list
res1 = list(zip(arr1, arr2))

# converting iterator to set
res2 = set(zip(arr1, arr2))

# it's possible to iterate over zip_obj (it's an iterable, after all)
for i, v in zip_obj:
    print(i, v)

print(f"{res1=}")
print(f"{res2=}")

# this is cool
print(f"{(5+5) * (1/2)=}")
