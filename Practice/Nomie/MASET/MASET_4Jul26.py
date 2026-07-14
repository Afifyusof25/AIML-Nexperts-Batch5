print("Hello, World")

# Variable - containers for data
name = "Alice"
age = 25
height = 5.6
is_student = True

# Display variable values
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Check data types
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

# Integers
num1 = 10
num2 = 20
sum_result = num1 + num2
print("Sum:", sum_result)

# Floats
price = 19.99
discount = 0.15
final_price = price * (1-discount)
print("Final Price:", final_price)
print("Rounded Final Price:", round(final_price, 2))
print("Formatted Final Price: {:.2f}".format(final_price))
print(f"Final Price using f-string: {final_price:.2f}")

# Diffent number operations
a = 15
b = 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b) # Returns the largest integer less than or equal to the division result
print("Modulus:", a % b) # Returns the remainder of the division
print("Exponentiation:", a ** b) # Returns a raised to the power of b   

# String basics
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# String formatting
age = 25
message = f"My name is {first_name} and I am {age} years old."
print(message)


# String methods
text = "  Hello, Python! " 
print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Strip:", text.strip())
print("Title Case:", text.title())
print("Capitalize:", text.capitalize())
print("Replace:", text.replace("Python", "World"))


# String indexing and slicing
word = "Python"
print("First character:", word[0]) # Indexing
print("Second character:", word[2])
print("Third Character:", word[3])
print("Last Character:", word[-1])
print("Substring or Slicing:", word[:4])
print("Substring:", word[0:2]) # From index 0 to 1


# Boolean values
is_sunny = True
is_raining = False

print("Is it sunny?", is_sunny)
print("Is it raining?", is_raining)



# Boolean operations
print("AND:", is_sunny and is_raining)
print("OR:", is_sunny or is_raining)
print("NOT:", not is_raining)

# Comparison results
age = 18
print("Age >= 18:", age >= 18)
print("Age == 20:", age == 20)
print("Age == 20:", age == 20 or age == 18)

# Mutli-line comments using triple quotes """
comments = """
This is a multi-line comments.
This is the second line of the comment.
"""
print(comments)


# Simple if-else statement
age = 18

if age >= 18:
    print("You are an adult.")
    print("You can vote.")

else:
    print("You are a minor.")
    print("You cannot vote.")   

print("Program completed successfully.\n")


# if-elif-else statement
score = 85
if score >= 90:
    grade = 'A'
    print("Excellent!")
elif score >= 80:
    grade = 'B'
    print("Good job!")
elif score >= 70:
    grade = 'C'
    print("You passed.")
else:
    grade = 'F'
    print("Need improvement.")

print("Your grade is:", grade)
print("\n")


# Nested if conditions
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license to drive")

else:
    print("YOu are too young to drive")

print("\n")
age = 17
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license to drive")

else:
    print("YOu are too young to drive")


print("="*30)
print("\n")
# Getting input from user
# name = input('Enter your name:')
# age = input("Enter your age: ")
# print(type(age))

# convert string to integer
# age = int(age)
# print(type(age))

# display output
# print(f"Hello, {name}! You are {age} years old.")
# print("Hello,", name, "! You are ", age, "years old.")
# print("Hello, " + name)


## MINI PROJECT 1
# 1. Ask user for total bill amount
total_bill_amount = float(input("Enter the total bill amount: RM"))

# 2. Ask user for number of people
number_of_people = int(input("Enter number of people: "))

# 3. Calculate amount per person
amount_per_person = total_bill_amount / number_of_people

# 4. Display result clearly
print(f"Each person needs to pay: RM{amount_per_person:.2f}")

print("="*30)
print("\n")


## MINI PROJECT 2
# 1. Asks the user for their name
name = str(input("Enter your name: "))

# 2. Asks for weight(kg) and height(m)
weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(m): "))

# 3. Calculate BMI using the formula (weight/height2)
BMI = weight / (height ** 2)

# 4. Determine and prints out the category based on BMI value

Health_Category = BMI
if BMI < 18.5:
    print("Health Category: Underweight ==== Please eat more to become healthy")
elif BMI < 25:
    print("Health Category: Normal weight ==== You're healthy!")
elif BMI < 30:
    print("Health Category: Overweight ==== Pls reduce your weight!")
elif BMI <35:
   print("Health Category: Obesity (Class 1) ==== Oh no! Pls go on diet!")
elif BMI < 40:
    print("Health Category: Obesity (Class 2) ==== Oh no! Pls go on diet!")
else:
    print("Health Category: Extreme Obesity ==== This is really not a good sign! Pls go on diet!!!!")

print(f"Your is BMI: {BMI:.2f}")
print("\n")
print("="*30)
print("\n")






