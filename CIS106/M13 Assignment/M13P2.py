def calculate_class_averages(grades_dict):
    """Calculates the class average for each of the three grade slots."""
    num_students = len(grades_dict)
    grade_totals = [0, 0, 0]

    for grades in grades_dict.values():
        for i in range(3):
            grade_totals[i] += grades[i]

    # Return a list of the three class averages
    return [total / num_students for total in grade_totals]

# Dictionary with student names and a list of three grades
student_grades = {
    "Alice": [90, 85, 88],
    "Bob": [78, 82, 80],
    "Charlie": [95, 92, 97],
    "Diana": [88, 90, 85],
    "Ethan": [88, 85, 90]
}

# Print individual student grade averages
print(f"{'Student Name':<15} {'Student Average':>15}")
print("-" * 31)

for name, grades in student_grades.items():
    student_avg = sum(grades) / len(grades)
    print(f"{name:<15} {student_avg:>15.2f}")

print("\n")

# Get and print the class average for each of the three grades
class_averages = calculate_class_averages(student_grades)

print(f"{'Assignment':<15} {'Class Average':>15}")
print("-" * 31)
for index, avg in enumerate(class_averages, start=1):
    print(f"Grade {index:<9} {avg:>15.2f}")