# Create a dictionary with student names as keys and grades as values
student_grades = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88
}

# Print table headers
print(f"{'Student Name':<15} {'Grade':>8}")
print("-" * 24)

# Print each student and their grade
total = 0
for name, grade in student_grades.items():
    print(f"{name:<15} {grade:>8.2f}")
    total += grade

# Calculate and print the class average
class_average = total / len(student_grades)
print("-" * 24)
print(f"{'Class Average':<15} {class_average:>8.2f}")