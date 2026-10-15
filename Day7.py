
"""
10 Days Python Challenge
DAY 7: SETS AND FROZENSETS

Topics:
1. Create sets
2. Remove duplicates
3. Add and remove elements
4. Set operations
5. Set comparisons
6. Membership testing
7. Loop through sets
8. Copy and update sets
9. Convert list to set
10. Frozen sets
11. Set comprehension
12. Practical examples
"""

print("=" * 55)
print("DAY 7: PYTHON SETS AND FROZENSETS")
print("=" * 55)


# --------------------------------------------------
# 1. CREATE A SET
# --------------------------------------------------

print("\n1. CREATE A SET")

numbers = {10, 20, 30, 40}

print("Set:", numbers)
print("Data type:", type(numbers))
print("Number of elements:", len(numbers))

# Sets store unique elements.
# Sets do not guarantee a particular iteration order.

duplicates = {10, 20, 10, 30, 20}
print("Set with duplicates removed:", duplicates)

# Create an empty set using set().
empty_set = set()
print("Empty set:", empty_set)
print("Empty set type:", type(empty_set))

# {} creates an empty dictionary, not an empty set.


# --------------------------------------------------
# 2. ADD ELEMENTS
# --------------------------------------------------

print("\n2. ADD ELEMENTS")

fruits = {"Apple", "Banana"}

print("Original:", fruits)

# add(): add one element
fruits.add("Mango")
print("After add():", fruits)

# Adding an existing element does not create a duplicate.
fruits.add("Apple")
print("After adding Apple again:", fruits)

# update(): add elements from an iterable
fruits.update(["Orange", "Grapes"])
print("After update():", fruits)


# --------------------------------------------------
# 3. REMOVE ELEMENTS
# --------------------------------------------------

print("\n3. REMOVE ELEMENTS")

colors = {"Red", "Green", "Blue"}

print("Original:", colors)

# remove(): raises KeyError if the item is missing
colors.remove("Red")
print("After remove():", colors)

# discard(): does not raise an error if missing
colors.discard("Yellow")
print("After discard of missing item:", colors)

# pop(): removes and returns an arbitrary element
removed = colors.pop()
print("Popped element:", removed)
print("After pop():", colors)

# clear(): remove all elements
colors.clear()
print("After clear():", colors)


# --------------------------------------------------
# 4. UNION
# --------------------------------------------------

print("\n4. UNION")

a = {1, 2, 3}
b = {3, 4, 5}

print("A:", a)
print("B:", b)

print("Union using |:", a | b)
print("Union using union():", a.union(b))

# Union contains all unique elements from both sets.


# --------------------------------------------------
# 5. INTERSECTION
# --------------------------------------------------

print("\n5. INTERSECTION")

print("Intersection using &:", a & b)
print("Intersection using intersection():",
      a.intersection(b))

# Intersection contains elements common to both sets.


# --------------------------------------------------
# 6. DIFFERENCE
# --------------------------------------------------

print("\n6. DIFFERENCE")

print("A - B:", a - b)
print("B - A:", b - a)

print("Using difference():", a.difference(b))

# A - B means elements in A but not in B.


# --------------------------------------------------
# 7. SYMMETRIC DIFFERENCE
# --------------------------------------------------

print("\n7. SYMMETRIC DIFFERENCE")

print("Using ^:", a ^ b)
print("Using symmetric_difference():",
      a.symmetric_difference(b))

# Includes elements in either set, but not both.


# --------------------------------------------------
# 8. SET COMPARISONS
# --------------------------------------------------

print("\n8. SET COMPARISONS")

x = {1, 2}
y = {1, 2, 3}
z = {7, 8}

print("Is x a subset of y?", x.issubset(y))
print("Is y a superset of x?", y.issuperset(x))
print("Are x and y disjoint?", x.isdisjoint(y))
print("Are x and z disjoint?", x.isdisjoint(z))
print("Are x and y equal?", x == y)


# --------------------------------------------------
# 9. MEMBERSHIP TESTING
# --------------------------------------------------

print("\n9. MEMBERSHIP TESTING")

languages = {"Python", "Java", "SQL"}

print("Python present?", "Python" in languages)
print("C++ present?", "C++" in languages)
print("Ruby absent?", "Ruby" not in languages)


# --------------------------------------------------
# 10. LOOP THROUGH A SET
# --------------------------------------------------

print("\n10. LOOP THROUGH A SET")

subjects = {"Python", "Java", "SQL"}

for subject in subjects:
    print(subject)

# The order may differ between runs.


# --------------------------------------------------
# 11. COPY AND UPDATE SETS
# --------------------------------------------------

print("\n11. COPY AND UPDATE")

original = {10, 20, 30}
copied = original.copy()

copied.add(40)

print("Original:", original)
print("Copied:", copied)

# Update the original using union.
original.update({40, 50})
print("After update():", original)

# intersection_update(): keep only common elements.
p = {1, 2, 3, 4}
p.intersection_update({3, 4, 5})
print("After intersection_update():", p)

# difference_update(): remove elements found in another set.
q = {1, 2, 3, 4}
q.difference_update({2, 4})
print("After difference_update():", q)

# symmetric_difference_update(): keep non-common elements.
r = {1, 2, 3}
r.symmetric_difference_update({3, 4, 5})
print("After symmetric_difference_update():", r)


# --------------------------------------------------
# 12. CONVERT A LIST TO A SET
# --------------------------------------------------

print("\n12. REMOVE DUPLICATES FROM A LIST")

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print("Original list:", numbers)
print("Unique elements:", unique_numbers)

# Convert back to a list if required.
unique_list = list(unique_numbers)
print("Unique list:", unique_list)

# Set iteration order is not guaranteed.


# --------------------------------------------------
# 13. FROZENSET
# --------------------------------------------------

print("\n13. FROZENSET")

fixed_numbers = frozenset([10, 20, 30, 20])

print("Frozen set:", fixed_numbers)
print("Data type:", type(fixed_numbers))
print("Number of elements:", len(fixed_numbers))

# Duplicate elements are removed.
# A frozenset cannot be changed after creation.

# These operations would raise AttributeError:
# fixed_numbers.add(40)
# fixed_numbers.remove(10)
# fixed_numbers.clear()

# But mathematical operations are allowed.
other_numbers = frozenset([30, 40, 50])

print("Union:", fixed_numbers | other_numbers)
print("Intersection:", fixed_numbers & other_numbers)
print("Difference:", fixed_numbers - other_numbers)


# --------------------------------------------------
# 14. SET COMPREHENSION
# --------------------------------------------------

print("\n14. SET COMPREHENSION")

numbers = [1, 2, 2, 3, 4, 4, 5]

squares = {n ** 2 for n in numbers}
print("Unique squares:", squares)

even_numbers = {n for n in numbers if n % 2 == 0}
print("Unique even numbers:", even_numbers)


# --------------------------------------------------
# 15. PRACTICAL EXAMPLE: COMMON STUDENTS
# --------------------------------------------------

print("\n15. PRACTICAL EXAMPLE")

python_students = {"Arun", "Priya", "Kumar"}
java_students = {"Priya", "Meena", "Kumar"}

print("Python students:", python_students)
print("Java students:", java_students)

print("Students in either course:",
      python_students | java_students)

print("Students in both courses:",
      python_students & java_students)

print("Only Python students:",
      python_students - java_students)

print("Only one of the two courses:",
      python_students ^ java_students)


# --------------------------------------------------
# COMPLETION
# --------------------------------------------------

print("\n" + "=" * 55)
print("DAY 7 COMPLETED SUCCESSFULLY!")
print("=" * 55)
