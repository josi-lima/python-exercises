from math import pi

# ================ SERPRO Training - day 02 ==============================


# 🚀 1.Create a list of fruits and access elements using indexing.

def selectFruits():
  fruits = ['strawberry', 'papaya', 'lemon', 'pineapple', 'banana', 'blueberry']
  
  print(fruits[1])    # papaya
  print(fruits[2:4])  # ['lemon', 'pineapple']
  print(fruits[-1])   # blueberry
selectFruits()

# ==================================================================

# 🚀 2. Given a list of numbers, find the sum and average.

def sumOfNums(numbers):
  sum = 0
  for num in numbers:
    sum += num
  print(f"Sum: {sum}. Average: {sum / 2}.")
  
sumOfNums([5, 7, 1, 4, 3, 10])  # Sum: 30. Average: 15.0  

# ==================================================================

#  🚀 3. Create a program that takes a temperature in Fahrenheit and converts it to Celsius.
#  Reminder: C = F – 32 / 1.8, starting by the subtraction.

def FahrToCelsius(degFahr):
  degCelsius = round(((degFahr - 32) / 1.8), 1)
  return degCelsius
print(FahrToCelsius(60))  # 15.6

# ==================================================================

# 🚀 4. Calculate the area and circumference of a circle given its radius.

# Note: formula to calculate the area: pi * radius ** 2.
# Note: formula to calculate the circumference: 2 * pi * radius.

def calculateCircle(radius):
  area = round((pi * radius ** 2), 2)
  circumference = round((2 * pi * radius), 2)
  
  print(f"Given the radius {radius}: the area is {area} and the circumference is {circumference}.")
calculateCircle(3.5)
# Given the radius 3.5: the area is 38.48 and the circumference is 21.99.

# ==================================================================

#  🚀 5. Create a function to reverse a given string.

def reverseStr(string):
  return string[::-1]
print(reverseStr('chocolate'))  # etalocohc

# ==================================================================

#  🚀 6. Given a list of names, concatenate them into a single string separated by spaces.

def concatNames(names):
  concat = ' '.join(names);
  return concat;
  
print(concatNames(['Jim', 'Kim', 'Lucy']))
# Jim Kim Lucy

# ==================================================================

#  🚀 7. Create a program that takes a sentence as input and counts the number of words in it.

def countWords(phrase):
  sentence = phrase.split()
  return len(sentence)
print(countWords('She said she would stay.'))  # 5
  
# ==================================================================

#  🚀 8. Create a function that will capitalize the first letter of each word in a text.

def capitalizeLetters(text):
  return text.title()
print(capitalizeLetters('movie: one day after tomorrow'))
# Movie: One Day After Tomorrow
   
# ==================================================================

#  🚀 9. Create a function to count the number of vowels in a given string.

def countVowels(text):
  count = {}
  vowels = {'a', 'e', 'i', 'o', 'u'}
  text = text.lower().replace('', ' ').split()
  
  for letter in text:
    if letter in vowels:
      if letter in count:
        count[letter] += 1
      else:
        count[letter] = 1
  return count
  
print(countVowels("I'm gonna make him an offer he can't refuse."));
# {'i': 2, 'o': 2, 'a': 4, 'e': 5, 'u': 1}

# ==================================================================




