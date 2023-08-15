# FUNCTIONS

# the reserved word 'def' is used to define a function 

# 🚀 1. Create a function that prints a message with the countries a person would like to live in.

def name_countries(country1, country2, country3):
  print(f"If I could live anywhere in the world, I'd move to {country1}, {country2} or {country3}.")
  
name_countries('Austria', 'Spain', 'Holland')
# If I could live anywhere in the world, I'd move to Austria, Spain or Holland.

# ===========================================================

# 🚀 2. Create a function that calculates an area of a triangle, base and height must not be zero.

def triangle_area(base, height):
  area = ''
  
  if base > 0 and height > 0:
    area = (base * height) / 2
    print(f"The area of the triangle is: {area}.")
  else:
    print("Please, insert a valid value.")
    
  return area

triangle_area(15, 10) 
# The area of the triangle is: 75.0.
  
# ===========================================================

# 🚀 3. Create a function that returns a string in all caps. 

def uppercase(string):
  upper = string.upper()
  return upper

print(uppercase("all we need is love."))
# ALL WE NEED IS LOVE.

# ---------------------------

# 🚀 4. Create a function that returns the names of a list in lower caps. 

heroes = ['BATMAN', 'SPIDER MAN', 'BLACK WIDOW']

def lowercase(name):
  lower = name.lower()
  return lower

for heroe in heroes:
  print(lowercase(heroe))
# batman 
# spider man 
# black widow

# ===========================================================

# 🚀 5. Create a dynamic function that multiplies two numbers, taken into account that the first number is the result of the sum of 'x + 2'.

def addTwo(x):
  return x + 2

def multiply(a, b):
  return a * b

# using a function as one of the parameters 

result = multiply(addTwo(20), 3)  # a = 22 / b = 3

print(result) # 66

# ===========================================================

# 🚀 6. Create a function that will convert degrees from Fahrenheit to Celsius.

def degreesFahr(temp):
  celsius = 0
  fahr = float(temp)
  
  celsius = round(((fahr - 32.0) * 5.0 / 9.0), 1)  # 1 is for one decimal place
  return celsius
  
print(f"Temperature in Celsius: {degreesFahr(63)} degrees.")
 
# ===========================================================

# 🚀 7. Create a function that returns a number entered by the user times 2.

def double_chances():
  user_input = input("What number would you like to double? ")
  print(int(user_input) * 2) 

double_chances()

# Note: the user's input will always be treated as a string
# int() converts the string provided to an integer

# ===========================================================

