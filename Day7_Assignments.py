
"""
Day 7 Assignment
Topic: Frozenset Operations Using For Loop

Learning objectives:
1. Create a frozenset
2. Iterate using a for loop
3. Display elements
4. Perform mathematical operations
5. Loop through union and intersection
6. Check membership
7. Understand immutability
"""


# --------------------------------------------------
# 1. CREATE A FROZENSET
# --------------------------------------------------

print("=" * 45)
print("1. CREATE A FROZENSET")
print("=" * 45)

numbers = frozenset([10, 20, 30, 40, 20])

print("Frozen set:", numbers)
print("Data type:", type(numbers))
print("Number of elements:", len(numbers))

# Duplicate values are automatically removed.


# --------------------------------------------------
# 2. ITERATE THROUGH A FROZENSET
# --------------------------------------------------

print("\n2. ITERATE THROUGH A FROZENSET")

for number in numbers:
    print(number)

# A frozenset does not guarantee a particular order.


# --------------------------------------------------
# 3. DISPLAY ELEMENTS WITH A MESSAGE
# --------------------------------------------------

print("\n3. DISPLAY ELEMENTS WITH A MESSAGE")

for number in numbers:
    print("Number:", number)


# --------------------------------------------------
# 4. CREATE TWO FROZENSETS
# --------------------------------------------------

print("\n4. CREATE TWO FROZENSETS")

set_a = frozenset([10, 20, 30, 40])
set_b = frozenset([30, 40, 50, 60])

print("Set A:", set_a)
print("Set B:", set_b)


# --------------------------------------------------
# 5. UNION USING A FOR LOOP
# --------------------------------------------------

print("\n5. UNION USING A FOR LOOP")

union_set = set_a | set_b

for number in union_set:
    print(number)

# Union contains all unique elements from both sets.


# --------------------------------------------------
# 6. INTERSECTION USING A FOR LOOP
# --------------------------------------------------

print("\n6. INTERSECTION USING A FOR LOOP")

intersection_set = set_a & set_b

for number in intersection_set:
    print("Common number:", number)

# Intersection contains only common elements.


# --------------------------------------------------
# 7. DIFFERENCE USING A FOR LOOP
# --------------------------------------------------

print("\n7. DIFFERENCE USING A FOR LOOP")

difference_set = set_a - set_b

for number in difference_set:
    print("Only in Set A:", number)


# --------------------------------------------------
# 8. CHECK MEMBERSHIP USING A FOR LOOP
# --------------------------------------------------

print("\n8. CHECK MEMBERSHIP")

search_number = 30
found = False

for number in set_a:
    if number == search_number:
        found = True
        break

if found:
    print(search_number, "was found.")
else:
    print(search_number, "was not found.")


# --------------------------------------------------
# 9. LOOP THROUGH STRINGS IN A FROZENSET
# --------------------------------------------------

print("\n9. FROZENSET OF STRINGS")

languages = frozenset(["Python", "Java", "SQL", "Python"])

for language in languages:
    print("Programming language:", language)


# --------------------------------------------------
# 10. FROZENSET CANNOT BE MODIFIED
# --------------------------------------------------

print("\n10. FROZENSET IMMUTABILITY")

fixed_numbers = frozenset([1, 2, 3])

print("Original frozen set:", fixed_numbers)

# The following operations are not supported:
# fixed_numbers.add(4)
# fixed_numbers.remove(1)
# fixed_numbers.clear()

print("Elements using a for loop:")

for number in fixed_numbers:
    print(number)

print("The frozenset remains unchanged.")


# --------------------------------------------------
# 11. PRACTICAL EXAMPLE: COURSE ENROLMENTS
# --------------------------------------------------

print("\n11. PRACTICAL EXAMPLE")

python_students = frozenset(["Arun", "Priya", "Kumar"])
java_students = frozenset(["Priya", "Meena", "Kumar"])

print("Students in both courses:")

for student in python_students & java_students:
    print(student)

print("Students in either course:")

for student in python_students | java_students:
    print(student)


# --------------------------------------------------
# COMPLETION
# --------------------------------------------------

print("\n" + "=" * 45)
print("DAY 7 ASSIGNMENT COMPLETED!")
print("=" * 45)
