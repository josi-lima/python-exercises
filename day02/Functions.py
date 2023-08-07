# FUNCTIONS
# the reserved word 'def' defines a function 

# Create a function that prints a message with the countries a person would like to live in.

def name_countries(country1, country2, country3):
  print(f"If I could live anywhere in the world, I'd move to {country1}, {country2} or {country3}.")
  
name_countries('Austria', 'Spain', 'Holland')
# If I could live anywhere in the world, I'd move to Austria, Spain or Holland.

# ===========================================================

# Create a function that calculates an area of a triangle, base and height must not be zero.

def triangle_area(base, height):
  area = ''
  
  if base > 0 and height > 0:
    area = (base * height) / 2
    print(f"The area of the triangle is: {area}.")
  else:
    print("Please, insert a valid value.")
    
  return area

triangle_area(15, 10) 
# The area of the triangle is: 75.0.
  
# ===========================================================

# Create a function that returns a string in all caps. 

def uppercase(string):
  upper = string.upper()
  return upper

print(uppercase("all we need is love."))
# ALL WE NEED IS LOVE.

# ---------------------------

# Create a function that returns the names of a list in lower caps. 

heroes = ['BATMAN', 'SPIDER MAN', 'BLACK WIDOW']

def lowercase(name):
  lower = name.lower()
  return lower

for heroe in heroes:
  print(lowercase(heroe))
# batman 
# spider man 
# black widow
  
# ===========================================================
