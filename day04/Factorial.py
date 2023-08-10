# Create a function that returns the value of the factorial of a number if it is defined, otherwise returns None.

# Note: in a set of 0 items (an empty set), there is only one way to arrange the items, therefore, 0! = 1

def factorial(num):
  
  if type(num) == int and num >= 0:
    factor = 1    
    for index in range(1, num):
      factor = (index + 1) * factor
    return factor
  else:
    return None
  
print(factorial(5)) # 120
print(factorial(0)) # 1
print(factorial(-2)) # None
print(factorial(1.3))  # None
print(factorial('spam')) # None

# ===========================================================

