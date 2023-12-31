class Dog:
  
  definition = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."
  
  # initialization function: whenever a new object is created from a class, this function is called. It's similar to a constructor in Java.
  def __init__(self):
    print("I'm alive!")
    
# ---------------------------

# an object or an instance of a class
Dog()  
# Output: I'm alive!

# ---------------------------
  
# access a variable from a class by using the dot operator

print(f"What is a dog? {Dog.definition}")
# Output: What is a dog? a domesticated carnivorous... 
