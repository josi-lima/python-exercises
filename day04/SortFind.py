# SORT in Python  -------  .sort() / .sorted()

# sort() modifies a list directly

# it can be less convenient than sorted(), but if you don't need the original list, it's slightly more efficient.

subjects = ['history', 'literature', 'arts', 'chemistry', 'physics']
subjects.sort()

print(subjects)
# ['arts', 'chemistry', 'history', 'literature', 'physics']

for sub in subjects:
  print(sub)
# arts chemistry history literature physics

# ---------------------------

# sort() also provides us the option to go in reverse easily. 
# instead of sorting in ascending order, we can do so in descending order.

fruits = ["Banana", "Strawberry", "Avocado", "Pineapple", "Grapes"]
fruits.sort(reverse = True)

print(fruits)
# ['Strawberry', 'Pineapple', 'Grapes', 'Banana', 'Avocado']

# ---------------------------

# sorted() generates a new list instead of modifying the one that already exists

design_patterns = ['factory', 'singleton', 'builder', 'adapter', 'decorator']
sorted_patterns = sorted(design_patterns)

print(design_patterns)
# ['factory', 'singleton', 'builder', 'adapter', 'decorator']

print(sorted_patterns)
# ['adapter', 'builder', 'decorator', 'factory', 'singleton']

# ---------------------------

# another difference is that the sort() method is only defined for lists. 
# in contrast, the sorted() function accepts any iterable, but it prints only the keys

data = {589: 'D', 423: 'B', 781: 'B', 946: 'E', 237: 'A'}

print(sorted(data))
# [237, 423, 589, 781, 946]

# ===========================================================

# FIND in Python

# find() method finds the first occurrence of the specified value 
# it returns -1 if the value is not found

word = "bananana"
i = word.find("na")
j = word.find("pi")

print(i)  # 2
print(j)  # -1

# ===========================================================
