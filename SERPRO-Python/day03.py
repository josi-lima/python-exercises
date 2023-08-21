import calendar
# importing calendar module for calendar operations 


# ================ SERPRO Training - day 03 ==============================


# 🚀 1. Write a program that checks if a given number is positive, negative, or zero.

def checkNumbers(num):
  if num > 0: return 'positive'
  elif num < 0: return 'negative'
  else: return 'zero'
print(checkNumbers(-5))  # negative
  
# ==================================================================

# 🚀 2. Create a loop that prints the first 10 even numbers.

def evenNumbers():
  for num in range(0, 10 + 1, 2):
    print(num)
evenNumbers()

# ==================================================================

# 🚀 3. Write a program that calculates the factorial of a given number.

def factorial(number):
  factor = 1
  for num in range(number):
    factor = (num + 1) * factor 
  return factor
print(factorial(5))   # 120

# ==================================================================

# 🚀 4. Create a program that takes a year as input and checks if it is a leap year or not.

def isLeapYear():
  year = int(input("Please, enter a year typing the four digits: "))
  
  if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    return 'leap year'
  else: return 'not a leap year'
print(isLeapYear())
  
# Notes:
# divided by 100 means century year (ending with 00) / century year divided by 400 is leap year.
# not divided by 100 means not a century year / # year divided by 4 is a leap year.

# ---------------------------------

def leapYear(year):
  check = calendar.isleap(year)
  return check
print(leapYear(2024)) # True

# ==================================================================

# 🚀 5. Given a list of integers, find all the even numbers and store them in a new list.

# ==================================================================

# 🚀 6. Given a list of names, print all names starting with the letter 'A'.

# ==================================================================

# 🚀 7. Implement a program that prints the multiplication table of a given number.

# ==================================================================

# 🚀 8. Given a list of words, count the number of words with more than five characters.

# ==================================================================

#  🚀 9. Write a program to check if a number is prime.

# ==================================================================

#  🚀 10. Calculate the compound interest for a given amount, interest rate, and time period.

# ==================================================================