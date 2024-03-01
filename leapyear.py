year = int(input("Enter a year: "))
# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#largest one
# Get user input for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
largest = max(num1, num2, num3)

# Print the result
print(f"The largest number is: {largest}")

#palindrome

def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]


# Get user input for the string
input_string = input("Enter a string: ")

# Check if it's a palindrome
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")

#
# Get user input for age
age = int(input("Enter your age: "))

# Determine the age group
if 0 <= age <= 12:
    print("You are a child.")
elif 13 <= age <= 19:
    print("You are a teenager.")
elif age >= 20 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior.")

#
import math

def calculate_triangle_area(side1, side2, side3):
    # Calculate the semi-perimeter
    s = (side1 + side2 + side3) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    return area

# Get user input for the lengths of the triangle sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the input forms a valid triangle
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    # Calculate and print the area
    area = calculate_triangle_area(side1, side2, side3)
    print(f"The area of the triangle is: {area}")
else:
    print("Invalid input. The given side lengths do not form a valid triangle.")

#
#import math

def calculate_triangle_area(side1, side2, side3):
    # Calculate the semi-perimeter
    s = (side1 + side2 + side3) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    return area

# Get user input for the lengths of the triangle sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the input forms a valid triangle
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    # Calculate and print the area
    area = calculate_triangle_area(side1, side2, side3)
    print(f"The area of the triangle is: {area}")
else:
    print("Invalid input. The given side lengths do not form a valid triangle.")

#
## Get user input for the score
score = float(input("Enter your score: "))

# Determine the grade
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    print("Invalid score. Please enter a score between 0 and 100.")
    exit()

# Print the result
print(f"Your grade is: {grade}")

#
#def determine_triangle_type(side1, side2, side3):
    # Check for equilateral triangle
    if side1 == side2 == side3:
        return "Equilateral"
    # Check for isosceles triangle
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    # If not equilateral or isosceles, it's a scalene triangle
    else:
        return "Scalene"

# Get user input for the lengths of the triangle sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the input forms a valid triangle
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    # Determine and print the type of the triangle
    triangle_type = determine_triangle_type(side1, side2, side3)
    print(f"The triangle is: {triangle_type}")
else:
    print("Invalid input. The given side lengths do not form a valid triangle.")

#
def is_leap_year(year):
    # Leap years are divisible by 4, but not by 100 unless also divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Get user input for the month and year
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

# Check if the input is valid
if 1 <= month <= 12:
    # Determine the number of days based on the month and year
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month in [4, 6, 9, 11]:
        days = 30
    else:
        # February: Check for leap year
        if is_leap_year(year):
            days = 29
        else:
            days = 28

    # Print the result
    print(f"The number of days in {month}/{year} is: {days}")
else:
    print("Invalid input. Please enter a valid month (1-12).")
