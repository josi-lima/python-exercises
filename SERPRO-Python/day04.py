# ================ SERPRO Training - day 04 ==============================


# 🚀 1. Write a program to check if a number is prime.

# prime numbers are numbers that can be divided only by one and by itself. There are 25 prime numbers in the range of 0 and 100.

def check_prime(number): 
  is_prime = True
  for i in range(2, number - 1):
    if int(number / i) == number / i:
      is_prime = False
  return is_prime
print(check_prime(97))   # True

# ==================================================================

# 🚀 2. Given a list of numbers, create a function to find the sum of all odd numbers.

def oddNumbers(numbers):
  sum = 0  
  for num in numbers:
    if num % 2 != 0:
      sum += num
  return sum
print(oddNumbers([3, 17, 2, 5, 10, 9, 4]))  # 34

# ==================================================================

# 🚀 3. Create a function to find the square of each element in a given list.

def squareNumbers(numbers):
  square = [num ** 2 for num in numbers]
  return square

print(squareNumbers([2, 4, 6, 8, 10, 12]))
# [4, 16, 36, 64, 100, 144]

# ==================================================================

# 🚀 4. Given a list of words, count the number of words with more than five characters.

def moreThan5(words):
  count = 0
  for word in words:
    if len(word) > 5:
      count += 1
  return count
print(moreThan5(['domino', 'table', 'booklet', 'cake', 'computer']))  # 3
  
# ==================================================================

# 🚀 5. Calculate the area of a triangle given its base and height. Base and height must be greater than 0. Area = base * height / 2

def calculateTriangle(base, height):
  if base > 0 and height > 0:
    area = (base * height) / 2
  else: return 'invalid input'
  return area
print(calculateTriangle(15, 20))    # 150.0

# ==================================================================

# 🚀 6. Create a function that takes a list of strings and returns the list sorted alphabetically.

def sortList(words):
  return sorted(words)
   
print(sortList(['brigadeiro', 'coxinha', 'beijinho', 'pizza']))
# ['beijinho', 'brigadeiro', 'coxinha', 'pizza']
  
# ==================================================================

# 🚀 7. Write a function that takes two lists and returns their intersection (common elements).


# ==================================================================

# 🚀 8. Create a function that takes a number as input and prints its multiplication table.


# ==================================================================

# 🚀 9. Create a function that will receive two lists of numbers as arguments and return a list composed of all the numbers that are either in the first list or second list, but not in both.


# ==================================================================

# 🚀 10. Create a loop that prints all prime numbers between 1 and 50.


# ==================================================================
