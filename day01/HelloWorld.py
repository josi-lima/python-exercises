# semicolons can be used to delimit statements coded on the same line

print('Hello World!'); print("Welcome to  planet Python!")

# ===========================================================

# Basic Data Types

# Python will automatically convert a type to another whenever required.
# No need to use the type casting like JAVA 

# integer (negative) 
temperature = -15 

# integer (positive)  
day = 6

# float
weight = 59.2 

# string
favePizzaTopping = "broccoli with dried tomatoes"

# string (with backslash)
faveRestaurant = 'Josie\'s Vegan Delicious "Burgers"'

# boolean
lightIsOn = True

if lightIsOn: 
  print("The light is on.")

# ===========================================================

# concatenation with a comma
print("The current temperature feels like:", temperature) 

# concatenation with F-strings
print(f"Today is August, the {day}th.")
print(f"Your total weight goal is: {weight - 5}.")
print(f"My favorite pizza topping is {favePizzaTopping}.")
print(f"My favorite restaurant of all time is {faveRestaurant}.")

# ===========================================================

# Assigning Values

# the same value can be assigned to multiple variables at the same time
numA = numB = numC = 1
print(numA, numB, numC)  # 1 1 1

# multiple variables can be assigned different values on a single line
boolean, luckyNum, name = True, 7, "John"
print(boolean, luckyNum, name)  # True 7 John

# ===========================================================
