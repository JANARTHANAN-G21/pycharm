# Get user input
number = float(input("Enter a number: "))

# Check the number and print the result
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Create a Python program that checks whether a given year is a leap year or not.
# (A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.)
# Get user input for the year

year = int(input("Enter a year: "))
# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")





