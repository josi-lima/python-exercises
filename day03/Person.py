# Defining a class with constructor and a method
class Person:
  
  # expand your init function to take in parameters beyond the parameter self  
  # 'self' = similiar to 'this'
  
  def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age
        
  # Declaring a method with if/else statement and returning a boolean
  # self -- passed as a parameter of a function inside a class, means that we have access to any attributes of the init function
  
  def isMinor(self):
      if self.age >= 18: # access the attribute 'age'
        return False
      else:
        return True
      
voter = Person('Josie', 'Brazilian', 38)

# access the attributes  
print(f"My name's {voter.name}. I'm a {voter.nationality} citizen, and I'm {voter.age} years old.")
# My name's Josie. I'm a Brazilian citizen, and I'm 38 years old.

# access the method
print(f"Is the voter a minor? {voter.isMinor()}")  # False


