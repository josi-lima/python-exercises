# slicing elements from a list

pizza = ['rúcula com tomate seco', '4 queijos', 'milho', 'frango vegano']

# index from 0 up to 2. The last one is not included, and index 0 can be omitted
print(pizza[:2])
# ['rúcula com tomate seco', '4 queijos']

# ===========================================================

# slicing characters from a string

quoteA = "So you failed." 

# index from 0 onwards, and from index 3 onwards
print(quoteA[:])
print(quoteA[3:])
# So you failed.
# you failed.

# ---------------------------

quoteB = "You wanna be really great? Then have the courage to fail big and stick around." 

# index from 0 up to 26. The last one is not included, and index 0 can be omitted
print(quoteB[:26])
# You wanna be really great?

# ---------------------------

quoteC = "Make them wonder why you're still smiling."

# index from 0 up to 16, the last one is not included
print(quoteC[0:16]) 
# Make them wonder

# ===========================================================




