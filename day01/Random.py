import random

# this module implements pseudo-random number generators 

# create a condition to print the evaluation of a service provided by a customer

magic_dice = random.randint(1,5)

print(f"Quality of service provided: {[magic_dice]}")

if magic_dice == 1: print("Poor service!")
elif magic_dice == 2: print("Reasonable!")
elif magic_dice == 3: print("Satisfactory!")
elif magic_dice == 4: print("Great!")
elif magic_dice == 5: print("Excelent!")

print("")
# ===========================================================

# create a condition to print a random fortune of the day from a fortune cookie

fortune_cookie = random.randint(1,50)

print(f"Let's check the fortune of the day:")

if fortune_cookie >= 41 and fortune_cookie <= 50: 
  print("Some days you are pigeon, some days you are statue.")
elif fortune_cookie >= 31:
  print("Your reality check's about to bounce.")
elif fortune_cookie >= 21: 
  print("Drive like hell, you will get there.")
elif fortune_cookie >= 11: 
  print("Okay to look at past and future. Just don't stare!")
elif fortune_cookie >= 1 and fortune_cookie >= 10:
  print("A day without sunshine is like night.")

# ===========================================================
