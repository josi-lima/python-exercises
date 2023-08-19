# =========== SERPRO Training - day 01 ==============================

# 🚀 1. Write a program to print "Hello, World!" 

def greeting():
  print("Hello World!")
greeting()

# ==================================================================
  
# 🚀 2. Calculate the sum of two numbers entered by the user.

def firstSum(numA, numB):
  return numA + numB;
print(firstSum(56, 44))  # 100

# ---------------------------

# def secondSum():
#   numA = int(input("Please, enter the first number: "))
#   numB = int(input("Please, enter the second number: "))
  
#   return numA + numB
# print(secondSum())

# ==================================================================

# 🚀 3. Convert temperature from Celsius to Fahrenheit.
# Reminder: C = F – 32 / 1.8, which means C * 1.8 + 32

def celsiusToFahr(temp):
  degCelsius = float(temp)
  
  degFahr = degCelsius * 1.8 + 32
  return degFahr
print(celsiusToFahr(23.4))   # 74.12

# ==================================================================

# 🚀 4. Write a program to calculate the area of a rectangle given its length and width.
# Note: the formula to calculate the area of a rectangle: "A (area) = l (length) * w (width)".

def calculateRecArea(length, width):
  area = float(length * width);
  return area;
print(calculateRecArea(5.5, 7.0))  # 38.5
  
# ==================================================================

# 🚀 5. Create a program that takes a user's name and age as input and prints a greeting message.

# def greetUser():
#   name = input("What's your first name? ")
#   age = input("How old are you? ")
  
#   print(f"Welcome, {name}! Today's your birthday! You're turning {age}.")
# greetUser()

# ==================================================================

# 🚀 6. Write a program to check if a number is even or odd.

def checkEvenOrOdd(number):
  if number % 2 == 0: return "even"
  else: return "odd"
print(checkEvenOrOdd(17))  # odd
  
# ==================================================================

# 🚀 7. Given a list of numbers, find the maximum and minimum values.

def findNumbers(numbers):
    
  min_value = min(numbers)
  max_value = max(numbers)
  
  print(min_value)  # 5
  print(max_value)  # 145
findNumbers([5, 24, 7, 63, 145, 88, 12, 37])

print(max(56, 89, 110, 23, 4, 38, 9, 72))  # 110
print(min(56, 89, 110, 23, 4, 38, 9, 72))  # 4

  
# Python’s built-in min() and max() functions: find the smallest and largest values in a single iterable or any number of regular arguments.

# ==================================================================

# 🚀 8. Create a Python function to check if a given string is a palindrome.

def isPalindrome(word):
  word = word.lower().replace(' ', '')
  return word == word[::-1]
print(isPalindrome('Was it a car or a cat I saw'))

# ---------------------------

# replaceAll() method of string values returns a new string with all matches of a pattern replaced by a replacement.

# for negative indexing, to display the 1st element to last element (in steps of 1) in reverse order, we use the [::-1].  
# https://www.freecodecamp.org/news/what-does-mean-in-python-operator-meaning-for-double-colon/

# ==================================================================

# 🚀 9. Given a list of integers, find the sum of all positive numbers.

def sumPositiveNums(numbers):
  sum = 0
  for num in numbers:
    if num > 0:
      sum += num
  return sum
print(sumPositiveNums([5, 2, 3, -1, -8, 2]))  # 12
       
# ==================================================================

# 🚀 10. Create a program that takes a sentence as input and counts the number of times a word appears in it.

def countWords(text):
  count = {}
  
  for word in text.lower().split():
    if word in count:
      count[word] += 1
    else:
      count[word] = 1
  print(count)
  
countWords("I would love to hear a love story about a place full of love");

# ==================================================================

# 🚀 11. Write a program that converts a given number of days into years, months and weeks.

def calendar(days):
  week = round((days / 7), 1)
  month = round((days / 30), 1)
  year = round((days / 365), 2)
  
  print(f"{days} day(s): {year} year(s).")
  print(f"{days} day(s): {month} month(s).")
  print(f"{days} day(s): {week} week(s).")

calendar(3)
  
# ==================================================================

# 🚀 12. Implement a program that swaps the values of two variables.

def swapValues(a, b):
  temporary = a  # temp = first
  a = b          # a = second
  b = temporary  # b = first
  print(a, b)
swapValues('first', 'second')

# ==================================================================


