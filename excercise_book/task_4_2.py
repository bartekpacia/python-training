# Write a program that puts
# numbers from 9 to 0 in a
# 10-element array

array = []
for i in range(9, -1, -1):
    array.append(i)

for number in array:
    print("array[" + str(i) + "] = " + str(i))
