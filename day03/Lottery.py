import random

class Lottery:
  
  def __init__(self):
    self.lucky_number = (random.randint(1, 100))  # instance variable

# variables that are unique in relation to one another
ticket1 = Lottery()
ticket2 = Lottery()

print(ticket1.lucky_number)
print(ticket2.lucky_number)

# creating an instance variable
ticket1.series = "526"

print(ticket1.series)  # 526
    

