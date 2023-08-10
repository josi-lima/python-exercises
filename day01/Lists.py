# LISTS

veggies = ['spinach', 'eggplant', 'pumpkin', 'zucchini']

# print an item of your list according to the index
print(f"The first item is {veggies[0]}.")  # spinach
print(f"The last item is {veggies[-1]}.")  # zucchini

# ---------------------------

# print the length of your list
print(f"How many veggies are there in your basket? {len(veggies)}.")  # 4

# ---------------------------

# make a clone from an existing list
vegetables = veggies[:]
print(vegetables)  # ['spinach', 'eggplant', 'pumpkin', 'zucchini']

# ---------------------------

# add a new item to the list
veggies.append('corn')
print(veggies)  # ['spinach', 'eggplant', 'pumpkin', 'zucchini', 'corn']

# ---------------------------

# add a new item to the list in a specific position
veggies.insert(2, 'pepper') # position, item
print(veggies)  
# ['spinach', 'eggplant', 'pepper', 'pumpkin', 'zucchini', 'corn']

# ---------------------------

# delete an item from the list in a specific position
del(veggies[0]); print(veggies)
# ['eggplant', 'pepper', 'pumpkin', 'zucchini', 'corn']

# ---------------------------

# iterating a list 

for veggie in vegetables:
  print(f"Don't forget to wash the {veggie} before eating it.")

# Don't forget to wash the spinach before eating it.
# Don't forget to wash the eggplant before eating it.
# Don't forget to wash the pumpkin before eating it.
# Don't forget to wash the zucchini before eating it.

# ---------------------------

# Working with Lists

countries = [
  'Portugal', 
  'England', 
  'Brazil', 
  'New Zealand', 
  'Spain'
  ]

numbers = [2, 14, 9, 10, 38]

# Sorting a List
countries.sort()
numbers.sort()

# Looping a List
for country in countries:
  print(country)
# Brazil England New Zealand Portugal Spain
    
for num in numbers:
  print(num)
# 2 9 10 14 38
    
# ===========================================================

