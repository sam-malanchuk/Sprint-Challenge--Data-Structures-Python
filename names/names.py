import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

namesTree = BinarySearchTree(names_1[len(names_1) // 2])

for names_1 in names_1:
    namesTree.insert(names_1)

for names_2 in names_2:
    if namesTree.contains(names_2):
        duplicates.append(names_2)

# Replace the nested for loops below with your improvements
# for name_1 in names_1: # O(n)
#     for name_2 in names_2: # O(n)
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Current Code: Runtime O(n^2)
# New code: Runtime O(n log n)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Understand: 
# Check two lists of 10,000 names and return the duplicates

# Plan:
# Create a search tree of of list one and search for every name from list 2

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
