
"""
Day 6 Assignment
Topic: Create Multiple Dictionaries and Merge Them
"""

print("=" * 50)
print("DAY 6: MERGE MULTIPLE DICTIONARIES")
print("=" * 50)


# --------------------------------------------------
# 1. CREATE MULTIPLE DICTIONARIES
# --------------------------------------------------

print("\n1. CREATE MULTIPLE DICTIONARIES")

student_personal = {
    "name": "Arun",
    "age": 20,
    "city": "Chennai"
}

student_academic = {
    "course": "Python",
    "mark": 90,
    "grade": "A"
}

student_contact = {
    "email": "arun@example.com",
    "phone": "9876543210"
}

print("Personal details:", student_personal)
print("Academic details:", student_academic)
print("Contact details:", student_contact)


# --------------------------------------------------
# 2. MERGE USING update()
# --------------------------------------------------

print("\n2. MERGE USING update()")

merged_update = student_personal.copy()

merged_update.update(student_academic)
merged_update.update(student_contact)

print("Merged dictionary:")
print(merged_update)


# --------------------------------------------------
# 3. MERGE USING THE | OPERATOR
# Python 3.9+
# --------------------------------------------------

print("\n3. MERGE USING | OPERATOR")

merged_pipe = (
    student_personal
    | student_academic
    | student_contact
)

print("Merged dictionary:")
print(merged_pipe)


# --------------------------------------------------
# 4. MERGE USING DICTIONARY UNPACKING (**)
# --------------------------------------------------

print("\n4. MERGE USING DICTIONARY UNPACKING")

merged_unpacking = {
    **student_personal,
    **student_academic,
    **student_contact
}

print("Merged dictionary:")
print(merged_unpacking)


# --------------------------------------------------
# 5. MERGE USING A FOR LOOP
# --------------------------------------------------

print("\n5. MERGE USING A FOR LOOP")

merged_loop = {}

for dictionary in (
    student_personal,
    student_academic,
    student_contact
):
    for key, value in dictionary.items():
        merged_loop[key] = value

print("Merged dictionary:")
print(merged_loop)


# --------------------------------------------------
# 6. HANDLE DUPLICATE KEYS
# --------------------------------------------------

print("\n6. HANDLE DUPLICATE KEYS")

dict1 = {
    "name": "Arun",
    "mark": 80
}

dict2 = {
    "mark": 95,
    "city": "Chennai"
}

merged_duplicate = dict1 | dict2

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged dictionary:", merged_duplicate)

# When a key appears in both dictionaries,
# the value from the right-hand dictionary wins.
# Therefore, mark becomes 95.


# --------------------------------------------------
# 7. MERGE MULTIPLE DICTIONARIES FROM A LIST
# --------------------------------------------------

print("\n7. MERGE DICTIONARIES FROM A LIST")

dict_a = {"a": 10, "b": 20}
dict_b = {"c": 30, "d": 40}
dict_c = {"e": 50, "f": 60}

dictionary_list = [dict_a, dict_b, dict_c]

final_dictionary = {}

for dictionary in dictionary_list:
    final_dictionary.update(dictionary)

print("Final dictionary:", final_dictionary)


# --------------------------------------------------
# 8. DISPLAY MERGED DATA USING A FOR LOOP
# --------------------------------------------------

print("\n8. DISPLAY FINAL STUDENT DETAILS")

for key, value in merged_update.items():
    print(key, ":", value)


# --------------------------------------------------
# 9. VERIFY THE MERGED RESULT
# --------------------------------------------------

print("\n9. VERIFY THE RESULT")

print("Total number of fields:", len(merged_update))
print("Student name:", merged_update["name"])
print("Student mark:", merged_update["mark"])
print("Student email:", merged_update["email"])

print("\nAssignment completed successfully!")
