
"""
10 Days Python Challenge
DAY 5: LIST OPERATIONS AND METHODS

Topics:
1. Create a list
2. Access list elements
3. Slice a list
4. Update list elements
5. Add elements
6. Remove elements
7. Sort and reverse
8. Search and count
9. Copy lists
10. Combine and compare lists
11. Built-in functions
12. List iteration
13. List comprehension
"""

print("=" * 50)
print("DAY 5: PYTHON LIST OPERATIONS")
print("=" * 50)


# --------------------------------------------------
# 1. CREATE A LIST
# --------------------------------------------------

print("\n1. CREATE A LIST")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)
print("Data type:", type(fruits))
print("Number of items:", len(fruits))


# --------------------------------------------------
# 2. ACCESS ELEMENTS
# --------------------------------------------------

print("\n2. ACCESS ELEMENTS")

print("First item:", fruits[0])
print("Second item:", fruits[1])
print("Last item:", fruits[-1])
print("Second-last item:", fruits[-2])

# Indexing starts at 0.
# Negative indexing starts from the end.


# --------------------------------------------------
# 3. SLICING
# --------------------------------------------------

print("\n3. LIST SLICING")

numbers = [10, 20, 30, 40, 50, 60]

print("Original:", numbers)
print("First three:", numbers[0:3])
print("Items from index 2:", numbers[2:])
print("First four:", numbers[:4])
print("Every second item:", numbers[::2])
print("Reversed copy:", numbers[::-1])


# --------------------------------------------------
# 4. UPDATE ELEMENTS
# --------------------------------------------------

print("\n4. UPDATE ELEMENTS")

colors = ["Red", "Green", "Blue"]

print("Before:", colors)

colors[1] = "Yellow"

print("After updating index 1:", colors)


# --------------------------------------------------
# 5. ADD ELEMENTS
# --------------------------------------------------

print("\n5. ADD ELEMENTS")

items = ["Pen", "Pencil"]

print("Original:", items)

# append(): add one item at the end
items.append("Eraser")
print("After append:", items)

# insert(): add an item at a specific index
items.insert(1, "Notebook")
print("After insert:", items)

# extend(): add multiple items
items.extend(["Scale", "Marker"])
print("After extend:", items)


# --------------------------------------------------
# 6. REMOVE ELEMENTS
# --------------------------------------------------

print("\n6. REMOVE ELEMENTS")

items = ["Pen", "Pencil", "Eraser", "Scale", "Marker"]

print("Original:", items)

# remove(): remove the first matching value
items.remove("Pencil")
print("After remove:", items)

# pop(): remove and return an item
removed_item = items.pop()
print("Popped item:", removed_item)
print("After pop:", items)

# pop(index): remove an item at an index
removed_item = items.pop(0)
print("Removed first item:", removed_item)
print("After pop(0):", items)

# del: delete by index or slice
del items[0]
print("After del:", items)

# clear(): remove all items
items.clear()
print("After clear:", items)


# --------------------------------------------------
# 7. SORT AND REVERSE
# --------------------------------------------------

print("\n7. SORT AND REVERSE")

numbers = [40, 10, 50, 20, 30]

print("Original:", numbers)

# sort(): modifies the original list
numbers.sort()
print("Ascending:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)

# reverse(): reverses the current order
numbers.reverse()
print("After reverse:", numbers)

# sorted(): returns a new sorted list
values = [5, 2, 8, 1]
sorted_values = sorted(values)

print("Original values:", values)
print("Sorted copy:", sorted_values)


# --------------------------------------------------
# 8. SEARCH AND COUNT
# --------------------------------------------------

print("\n8. SEARCH AND COUNT")

fruits = ["Apple", "Banana", "Mango", "Banana"]

print("Fruits:", fruits)

# index(): first matching item's index
print("Index of Banana:", fruits.index("Banana"))

# count(): number of occurrences
print("Banana count:", fruits.count("Banana"))

# in: check membership
print("Is Mango present?", "Mango" in fruits)
print("Is Grapes present?", "Grapes" in fruits)


# --------------------------------------------------
# 9. COPY A LIST
# --------------------------------------------------

print("\n9. COPY A LIST")

original = [10, 20, 30]

# Assignment creates another reference
same_list = original

# copy() creates a separate shallow copy
copied_list = original.copy()

same_list.append(40)
print("Original after same_list.append:", original)

copied_list.append(50)
print("Original after copied_list.append:", original)
print("Copied list:", copied_list)

# Use copy() when you need an independent
# shallow copy of a list of simple values.


# --------------------------------------------------
# 10. COMBINE AND REPEAT LISTS
# --------------------------------------------------

print("\n10. COMBINE AND REPEAT")

a = [1, 2, 3]
b = [4, 5, 6]

print("Combined:", a + b)
print("Repeated:", a * 2)


# --------------------------------------------------
# 11. BUILT-IN FUNCTIONS
# --------------------------------------------------

print("\n11. BUILT-IN FUNCTIONS")

marks = [85, 90, 75, 95, 80]

print("Marks:", marks)
print("Length:", len(marks))
print("Minimum:", min(marks))
print("Maximum:", max(marks))
print("Total:", sum(marks))
print("Sorted:", sorted(marks))

average = sum(marks) / len(marks)
print("Average:", average)


# --------------------------------------------------
# 12. LOOP THROUGH A LIST
# --------------------------------------------------

print("\n12. LOOP THROUGH A LIST")

for fruit in fruits:
    print(fruit)

print("\nItems with their positions:")

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# --------------------------------------------------
# 13. LIST COMPREHENSION
# --------------------------------------------------

print("\n13. LIST COMPREHENSION")

numbers = [1, 2, 3, 4, 5, 6]

# Create a list of squares
squares = [n * n for n in numbers]
print("Squares:", squares)

# Select only even numbers
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)


# --------------------------------------------------
# 14. NESTED LIST
# --------------------------------------------------

print("\n14. NESTED LIST")

students = [
    ["Arun", 90],
    ["Priya", 85],
    ["Kumar", 95]
]

print("First student:", students[0])
print("First student's name:", students[0][0])
print("First student's mark:", students[0][1])

for student in students:
    print(student[0], "scored", student[1])


# --------------------------------------------------
# 15. CHECK EMPTY LIST
# --------------------------------------------------

print("\n15. CHECK EMPTY LIST")

my_list = []

if not my_list:
    print("The list is empty.")
else:
    print("The list contains items.")


# --------------------------------------------------
# COMPLETION
# --------------------------------------------------

print("\n" + "=" * 50)
print("DAY 5 COMPLETED!")
print("=" * 50)
