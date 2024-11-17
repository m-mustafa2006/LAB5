# Program to print the multiplication table of a user-entered number
number = int(input("Enter a number for the multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
