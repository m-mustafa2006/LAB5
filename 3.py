# Program to print the first 10 natural numbers and their sum
print("The first 10 natural numbers are:")
total_sum = 0
for i in range(1, 11):
    print(i, end=" ")  # Print numbers on the same line
    total_sum += i  # Add the number to the total sum
print("\nThe Sum is:", total_sum)
