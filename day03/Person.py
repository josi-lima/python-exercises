# Defining a class with constructor and a method
class Person:
  
  # expand your init function to take in parameters beyond the parameter self  
  # 'self' = similiar to 'this'
  
  def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age
        
  # Declaring a method with if/else statement and returning a boolean
  def isMinor(self):
      if self.age >= 18: # access the parameter
        return False
      else:
        return True

candidate = Person('Josie', 'Brazilian', 38)
  
print(candidate.name); print(candidate.nationality); print(candidate.age)

