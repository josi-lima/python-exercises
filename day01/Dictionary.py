# DICTIONARIES

# They are lists of Key: Value pairs, and can contain heterogeneous keys as well as values.

room_nums = {
  'Tom': 403, 
  'Jerry': 596}

# ---------------------------

# alter a value, set the value associated with the ’Tom’ key to 753
room_nums['Tom'] = 753  

print(room_nums) 
# {'Tom': 753, 'Jerry': 596}

# ---------------------------

# print only one specific value
print(room_nums['Jerry'])  
# 596

# ---------------------------

# add a new key, add the key ’Isaac’ with the associated value
room_nums['Isaac'] = 345  

print(room_nums.keys()) 
# dict_keys(['Tom', 'Jerry', 'Isaac'])

# ---------------------------

# test if ’issac’ is in the dictionary
print ('Isaac' in room_nums)   # key in my_dic
# True

# ---------------------------

# delete a Key: Value pair from a dictionary
del(room_nums['Jerry'])
print(room_nums) 
# {'Tom': 753, 'Isaac': 345}

# ---------------------------

# it's possible to have different types of values in a single list

hotel_features = {
  1: 'Taj', 
  'city': 'Woodland', 
  'distance': 3.14}

print(hotel_features)
# {1: 'Taj', 'city': 'Woodland', 'distance': 3.14}

# ===========================================================

# Iterating a dictionary

# loop over the keys in the dictionary, rather than the keys and values

states_Brazil = {
  'SP': 'Sao Paulo', 
  'CE': 'Ceará', 
  'RS': 'Rio Grande do Sul'
  }

for key in states_Brazil:
  print(f"{key}: corresponds to {states_Brazil[key]}.") # 'key' is just a variable name.
  
# Example --> RS: corresponds to Rio Grande do Sul.

# ---------------------------

# now loop over both keys and values
# dict.items() returns a copy of the dictionary’s list in the form of (key, value) tuple pairs.

for key, value in states_Brazil.items():   # 'key' and 'value' are just variable names.
  print(f"{key} is the acronym for {value}.")
  
# Example --> SP is the acronym for Sao Paulo.
  
# ===============================================

