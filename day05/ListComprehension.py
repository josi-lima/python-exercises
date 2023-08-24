# ======= LIST COMPREHENSION ===========

# list comprehension -- allows you to essentially make a for loop in one line while returning a copy of the list that you're iterating over. 

# It also allows you to filter or call functions on every item or of a list. 

# ---------------------------

numbers = [1, 2, 3, 4, 5]

# [ output (do this) / collection (for this collection) ]
multiply = [2 * num for num in numbers]

print(multiply)
# [2, 4, 6, 8, 10]

# ===========================================================

# list comprehension with filter

words = ['pen', 'sweter', 'bowl', 'window', 'sun']

# [ output (do this) / collection (for this collection) / condition (is this situation) ]
words_s = [word for word in words if word[0].lower() == 's'.lower() ]

print(words_s)
# ['sweter', 'sun']

# ---------------------------

# list comprehension with range

my_list = list(range(1, 100))

filtered_list = [item for item in my_list if item % 10 == 0]

print(filtered_list)
# [10, 20, 30, 40, 50, 60, 70, 80, 90]

# ===========================================================

# cleaning the text with list comprehension, split() and replace()

phrase = "My name is Josie. I love French fries."

print(phrase.split())
# ['My', 'name', 'is', 'Josie.', 'I', 'love', 'French', 'fries.']

# return the sentence without any periods
def cleanText(word):
  return word.replace('.', '').lower()
clean_text01 = [ cleanText(word) for word in phrase.split() ]

print(clean_text01)
# ['my', 'name', 'is', 'josie', 'i', 'love', 'french', 'fries']

# ===========================================================

# working with list comprehension on texts

text = "Officials in Hebei Province, which borders Beijing, had opened flood gates and spillways in seven low-lying flood control zones to prevent rivers and reservoirs from overflowing in Beijing and the region's other metropolis, Tianjin, state media said."

clean_text02 = text.replace('.', '').split()

# return the words that are 5-characters-long
short_words = [word for word in clean_text02 if len(word) == 5]

print(short_words)
# ['Hebei', 'which', 'flood', 'gates', 'seven', 'flood', 'zones', 'other', 'state', 'media']

# ===========================================================

# if / else statements with list comprehension

conditional_list = ['Monty Python' if n % 6 == 0 else 'Python' if n % 3 == 0 else 'Monty' if n % 2 == 0 else n for n in range(1, 10)]

print(conditional_list)
# [1, 'Monty', 'Python', 'Monty', 5, 'Monty Python', 7, 'Monty', 'Python']

# ===========================================================
