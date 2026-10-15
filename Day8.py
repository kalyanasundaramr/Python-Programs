
# =====================================================
# DAY 8: FUNCTIONS IN PYTHON - COMPLETE PRACTICE
# =====================================================

# 1. Simple function
def welcome():
    print("\nWelcome to Day 8: Python Functions!")


# 2. Function with parameters
def greet(name):
    print(f"Hello, {name}!")


# 3. Function with return
def add(a, b):
    return a + b


# 4. Default parameter
def power(number, exponent=2):
    return number ** exponent


# 5. Keyword arguments
def student_details(name, age, city="Chennai"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


# 6. Variable positional arguments
def calculate_sum(*numbers):
    return sum(numbers)


# 7. Variable keyword arguments
def show_information(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


# 8. List as an argument
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# 9. Dictionary as an argument
def display_dictionary(data):
    for key, value in data.items():
        print(f"{key}: {value}")


# 10. Lambda function
square = lambda number: number ** 2


# 11. Recursive function
def factorial(n):
    if n < 0:
        raise ValueError("Number must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# 12. Grade calculator
def calculate_grade(marks):
    if not 0 <= marks <= 100:
        return "Invalid marks"
    elif marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "E"


# 13. Main program
def main():
    welcome()

    print("\n--- Greeting ---")
    greet("Arun")
    greet("Priya")

    print("\n--- Addition ---")
    print("10 + 20 =", add(10, 20))

    print("\n--- Default Arguments ---")
    print("Square of 5:", power(5))
    print("Cube of 5:", power(5, 3))

    print("\n--- Keyword Arguments ---")
    student_details(age=25, name="Kumar")

    print("\n--- *args ---")
    print("Sum:", calculate_sum(10, 20, 30, 40))

    print("\n--- **kwargs ---")
    show_information(
        name="Priya",
        age=22,
        city="Chennai"
    )

    print("\n--- List and Average ---")
    marks = [85, 90, 78, 92]
    print("Marks:", marks)
    print("Average:", calculate_average(marks))

    print("\n--- Dictionary ---")
    student = {
        "name": "Arun",
        "marks": 95,
        "city": "Chennai"
    }
    display_dictionary(student)

    print("\n--- Lambda ---")
    print("Square of 6:", square(6))

    print("\n--- Recursion ---")
    print("Factorial of 5:", factorial(5))

    print("\n--- Grade Calculator ---")
    print("Marks 95:", calculate_grade(95))
    print("Marks 72:", calculate_grade(72))
    print("Marks 45:", calculate_grade(45))
    print("Marks 110:", calculate_grade(110))


if __name__ == "__main__":
    main()
