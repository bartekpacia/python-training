# Write a program that puts
# numbers from 0 to 9 in a 
# 10-element array

array = []

for i in range(0, 10):
    array.append(i)

for i in array:
    print("array[" + str(i) + "] = " + str(i))