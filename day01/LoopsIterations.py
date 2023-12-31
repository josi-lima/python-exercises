# FOR LOOP

# loop starts in 1 and goes until 4 (non-inclusive)
for count_down in range(1, 4): 
  print("The race starts in: " + str(count_down)) # concatenation with a + symbol
print("Goooo!!") 

# The race starts in: 1
# The race starts in: 2
# The race starts in: 3
# Goooo!!

# ===========================================================

# the counter variable {position} is incremented by 2 each time the loop repeats
# starting position, ending position, increment

for position in range(5, 10, 2):
  print(f"Your position on the pulic exams is: {position}th.")
  
# Your position on the pulic exams is: 5th.
# Your position on the pulic exams is: 7th.
# Your position on the pulic exams is: 9th. 

# ===========================================================

# loop 10 times and print the number of the loop * 2. Ex. 2, 4, 6, 8..., 20.
for num in range(10):
  multiply = (num + 1) * 2;
  print(multiply)

# ===========================================================

# the counter variable {monkeys} is decreased by 2 each time the loop repeats
# starting position, ending position, decrement

for monkeys in range(10, 4, -2):
  print(f"Now there are only {monkeys} monkeys jumping on the bed.")
  
# now there are only 10 monkeys jumping on the bed.
# now there are only 8 monkeys jumping on the bed.
# now there are only 6 monkeys jumping on the bed.

# ===========================================================

# Iterations / for in

# Iterating a string

for n in "banana":
    print(n)  
# b
# a
# n
# a
# n
# a
    
# ---------------------------

# Iterating a List

friends = ['Monica', 'Ross', 'Chandler', 'Rachel', 'Joey', 'Phoebe']

for friend in friends:
  print(f"I'll be there for you, {friend}.")
print("When the rain starts to pour...")

# ---------------------------

# Iterating a Tuple

yummy_food = ('vegan barbecue', 'samosa', 'ice cream')

for food in yummy_food:
  print(f"If you eat too much {food}, you'll be chubby!")
  
# unlike the list, a tuple is immutable, and is like a static array

# ===========================================================

# WHILE with conditionals

numberA = 0

while True:
  if numberA == 3:
      break
  numberA = numberA + 1
  
  print(numberA)  # 1 2 3
    
# ---------------------------

numberB = 0

while True:
  if numberB == 3:
      break
  
  print(numberB)  # 0 1 2
  numberB = numberB + 1
  
# ===========================================================

# WHILE LOOPS

number = 3 # declaring the start point

while number < 10:
  number *= 2
  print (number) # 6 12
print ("Exited while loop.")

# We can exit any loop by using the break statement
while True:
  userInput = input("Please enter 'go away': ")
  if userInput.strip() == 'go away':
    print("Thanks! Have a good life!")
    break
  
# the strip() method removes any leading (at the beginning of the string), and trailing (at the end) whitespaces.
  
# ===========================================================


  
