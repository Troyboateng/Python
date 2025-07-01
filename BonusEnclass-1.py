# Write a program that gets 5 numbers (using loop) and only prints a message for each one if it is a 3 digit number.

# Additionally, the program should calculate and display the sum of all the 3-digit numbers entered.

sum_of_numbers = 0

for i in range(2):
    number = int(input(f"Enter a 3-digit number {i+1}: "))
    
    if number >= 100 and number <= 999:
        print(f"The number {number} is a 3-digit number.")
        sum_of_numbers += number
print(f"The sum of numbers is {sum_of_numbers}")
        