# WORD COUNTER

vowels = " a e i o u a a o e "

# ---------------------------

# split() takes the string and, anywhere that there's a space, it breaks it off into single strings inside of a list.

print(vowels.split())
# ['a', 'e', 'i', 'o', 'u', 'a', 'a', 'o', 'e']

# with a dictionary, we can store the words (or, in this case, these letters) as the keys, and then count how many times each letter appears as an integer.
word_count = {}

# loop over the list that comes from vowels.split() and count it string

for letter in vowels.split():
  if letter in word_count:
    word_count[letter] += 1
  else: 
    word_count[letter] = 1
  
print(word_count)
# {'a': 3, 'e': 2, 'i': 1, 'o': 2, 'u': 1}

# ===========================================================

# Create a program that counts how many times a word appears in a certain text.

# triple quotes: it allows you to use multi-lines and have it be all one string.

text = """ For days, the rain came down in sheets, pounding Beijing and areas around it in what the government said was the heaviest deluge China's capital had seen since record keeping began 140 years ago.

When the extreme downpour finally stopped on Tuesday, most of Beijing had been spared the worst — but partly because officials made sure the floodwaters went elsewhere.

Officials in Hebei Province, which borders Beijing, had opened flood gates and spillways in seven low-lying flood control zones to prevent rivers and reservoirs from overflowing in Beijing and the region's other metropolis, Tianjin, state media said. 

The Communist Party leader of Hebei, Ni Yuefeng, said he ordered the "activation of flood storage and diversion areas in an orderly manner, so as to reduce the pressure on Beijing's flood control and resolutely build a 'moat' for the capital." (from The New York Times) """

# ---------------------------

# print the length of a text, counting its characters
print(len(text))  # 890

# ---------------------------

# whenever there's a space, break the longer string off into single strings inside of a list.
print(text.split())

# Example: ['For', 'days,', 'the', 'rain', 'came', 'down', ... ]

# ---------------------------

# print the number of words in a text, counting its strings
print(len(text.split()))  # 144
