# Dictionaries

# They are lists of Key: Value pairs, and can contain heterogeneous keys as well as values.

room_nums = {'Tom': 403, 'Jerry': 596}
room_nums['Tom'] = 753  # set the value associated with the ’Tom’ key to 753

print(room_nums) 
# {'Tom': 753, 'Jerry': 596}

print(room_nums['Jerry'])  
# 596

room_nums['Isaac'] = 345  # add a new key ’Isaac’ with the associated value

print(room_nums.keys()) 
# dict_keys(['Tom', 'Jerry', 'Isaac'])

# test if ’issac’ is in the dictionary
print ('Isaac' in room_nums)   # key in my_dic
# True

# different types of values in a single list
hotel_features = {1: "Taj", "city": "Woodland", "distance": 3.14}

print(hotel_features)
# {1: 'Taj', 'city': 'Woodland', 'distance': 3.14}

