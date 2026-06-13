# ============================================================
# Assignment 2 — Python Basics
# ============================================================

# ─────────────────────────────────────────────
# 1. Sum of first 10 natural numbers
# ─────────────────────────────────────────────
print("=" * 45)
print("1. Sum of First 10 Natural Numbers")
print("=" * 45)

total = 0
for i in range(1, 11):
    total += i

print(f"Numbers : 1 to 10")
print(f"Sum     : {total}")


# ─────────────────────────────────────────────
# 2. Factorial of a number
# ─────────────────────────────────────────────
print("\n" + "=" * 45)
print("2. Factorial of a Number")
print("=" * 45)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = 6
print(f"Factorial of {num} = {factorial(num)}")
print(f"Factorial of 0 = {factorial(0)}")
print(f"Factorial of 5 = {factorial(5)}")


# ─────────────────────────────────────────────
# 3. Fibonacci Series
# ─────────────────────────────────────────────
print("\n" + "=" * 45)
print("3. Fibonacci Series (First 10 terms)")
print("=" * 45)

def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

fib = fibonacci(10)
print(f"Series : {fib}")


# ─────────────────────────────────────────────
# 4. Largest among 3 numbers
# ─────────────────────────────────────────────
print("\n" + "=" * 45)
print("4. Largest Among 3 Numbers")
print("=" * 45)

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a, b, c = 45, 78, 23
print(f"Numbers : {a}, {b}, {c}")
print(f"Largest : {find_largest(a, b, c)}")


# ─────────────────────────────────────────────
# 5. Student Result System
# ─────────────────────────────────────────────
print("\n" + "=" * 45)
print("5. Student Result System")
print("=" * 45)

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F (Fail)"

def student_result(name, roll_no, marks_list, total_marks_per_subject=100):
    num_subjects = len(marks_list)
    total_obtained = sum(marks_list)
    total_max = total_marks_per_subject * num_subjects
    percentage = (total_obtained / total_max) * 100
    grade = get_grade(percentage)

    print(f"\n  Student Name   : {name}")
    print(f"  Roll No        : {roll_no}")
    print(f"  Marks Obtained : {marks_list}")
    print(f"  Total          : {total_obtained} / {total_max}")
    print(f"  Percentage     : {percentage:.2f}%")
    print(f"  Grade          : {grade}")
    print(f"  Result         : {'PASS ✅' if grade != 'F (Fail)' else 'FAIL ❌'}")

# Example students
student_result("Ananya", "101", [85, 90, 78, 92, 88])
student_result("Rohan",  "102", [45, 50, 38, 42, 55])
student_result("Priya",  "103", [95, 98, 92, 97, 99])

print("\n" + "=" * 45)
print("  All tasks completed!")
print("=" * 45)
