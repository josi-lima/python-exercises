# SETS

# Set is one of 4 built-in data types in Python used to store collections of data
# the other 3 are List, Tuple, and Dictionary

# a set object is not subscriptable
# so you can't use the slice method to fecth items from a set, for example 

# ---------------------------

# a set cannot contain duplicated items
# de-duplicating items from a set 

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket) 
# {'orange', 'apple', 'pear', 'banana'}   

# ---------------------------

# de-duplicating items from a list by using the set constructor

furniture = ['couch', 'chair', 'bed', 'couch', 'bed']
furniture = list(set(furniture))

print(furniture)
# ['couch', 'chair', 'bed']

# ===========================================================

# demonstrate set operations on unique letters from two words

a = set('josiane')
b = set('renato')

print(a) # unique letters in a
# {'a', 's', 'i', 'j', 'o', 'e', 'n'}

print(a - b)  # letters in a, but not in b
# {'i', 's', 'j'}

print(a | b)  # letters in a or b, or both
# {'a', 't', 's', 'i', 'r', 'j', 'o', 'e', 'n'}

print(a & b)   # letters in both a and b
# {'a', 'e', 'n', 'o'}

print(a ^ b)   # letters in a or b, but not both
# {'i', 'r', 'j', 's', 't'}

# ===========================================================

# define a set also by passing any sort of iterable object in the constructor of the set class
# sets are unordered, we may get a different order each time we print

# a set from a list
places = set(['beach', 'park', 'church'])

print(places)
# {'beach', 'park', 'church'}

# ---------------------------

# a set from a tuple
desserts = set(('ice cream', 'lemon pie', 'chocolate cake'))

print(desserts)
# {'lemon pie', 'chocolate cake', 'ice cream'}

# ---------------------------

# a set from a dictionary prints only the keys
city = set({'Los Angeles': 'CA', 'New York': 'NY', 'Tampa': 'FL'})

print(city)
# {'Tampa', 'Los Angeles', 'New York'}

# ===========================================================

# add and remove an element from a set
city.add('São Paulo')
print(city)
# {'São Paulo', 'Los Angeles', 'Tampa', 'New York'}

city.remove('Tampa')
print(city)
# {'São Paulo', 'Los Angeles', 'New York'}

# add() method differs from append(). 
# add() does not add an element at the last position since the data type set is unordered

# ===========================================================



