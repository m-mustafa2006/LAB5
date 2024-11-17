# Program to print the first 10 natural numbers and their sum
print("The first 10 natural numbers are:")
total_sum = 0
for i in range(1, 11):
    print(i, end=" ")
    total_sum += i
print("\nThe Sum is:", total_sum)
