# semicolons can be used to delimit statements coded on the same line

print('Hello World!'); print("Welcome to planet Python!")

# ===========================================================

# Basic Data Types

# Python will automatically convert a type to another whenever required.
# No need to use the type casting like JAVA 

# ---------------------------

# integer (negative) 
temperature = -15 

# ---------------------------

# integer (positive)  
day = 6

# ---------------------------

# float
weight = 59.2 

# ---------------------------

# string
fave_pizza_topping = "broccoli with dried tomatoes"

# string (with backslash)
fave_restaurant = 'Josie\'s Vegan Delicious "Burgers"'

# ===========================================================

# boolean

light_is_on = True
party_is_over = False  

if light_is_on or party_is_over:  # this condition is true. The statement will be printed.
  print("Time is up! Let's go home.")

light_is_on = False
party_is_over = False

if light_is_on | party_is_over:  # this condition is false. Nothing will be printed.
  print("Show's over! Let's go to bed.")
  
# the symbol | indicates logical disjunction, also called logical alternation, is an operation on two logical values, typically the values of two propositions, that produces a value of false if, and only if, both of its operands are false.

# ---------------------------

# check bool values
checkA = 0 == 0.0
print(checkA)  # True

# ---------------------------

# casting booleans
checkB = bool(-1) == 1
print(checkB) # True
print(bool(0))  # False
# negative numbers are also True, but 0 is False

# empty strings, lists or dictionaries are False
print(f"Empty string is: {bool('')}")
print(f"Empty list is: {bool([])}")
print(f"Empty dictionary is: {bool({})}")

# ===========================================================

# concatenation with a comma
print("The current temperature feels like:", temperature) 

# concatenation with F-strings
print(f"Today is August, the {day}th.")
print(f"Your total weight goal is: {weight - 5}.")
print(f"My favorite pizza topping is {fave_pizza_topping}.")
print(f"My favorite restaurant of all time is {fave_restaurant}.")

# ===========================================================

# Assigning Values

# the same value can be assigned to multiple variables at the same time
numA = numB = numC = 1
print(numA, numB, numC)  # 1 1 1

# multiple variables can be assigned different values on a single line
boolean, lucky_num, name = False, 7, "John"
print(boolean, lucky_num, name)  # False 7 John

# ===========================================================

# unlike addition, you can multiple a string and an integer.

multiply = '4' * 4

print(multiply)  # '4444'

# ===========================================================
