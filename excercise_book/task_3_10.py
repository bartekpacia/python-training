# Write a program that calculates
# the sum of all even numbers from 1
# to 100 using a for loop

sum = 0

for i in range(0, 101, 2):
    sum = sum + i

print(sum)