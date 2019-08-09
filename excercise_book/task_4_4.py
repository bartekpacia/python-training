# Write a program that creates
# a two-dimensional array, places
# numbers from 0 to 9
# on the diagonal and places 0
# out of the diagonal.
# It must also calculate the sum
# of elements on the diagonal.

columns = 10
rows = 10
array = [[0 for i in range(columns)] for j in range(rows)]


for i in range(rows):
    array[i][i] = i

for i in range(rows):
    print(array[i])

sum = 0

for i in range(rows):
    sum = sum + array[i][i]

print("Sum of elements on the diagonal: " + str(sum))
