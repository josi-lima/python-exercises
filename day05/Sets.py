# SETS

# Set is one of 4 built-in data types in Python used to store collections of data,
# the other 3 are List, Tuple, and Dictionary

# ---------------------------

# a set cannot contain duplicated items
# de-duplicating items from a set 

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket) 
# {'orange', 'apple', 'pear', 'banana'}   

# ---------------------------

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

# ---------------------------






