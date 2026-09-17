# Problem 1: Exam Score Calculator

# Get exam scores from the user
exam1 = float(input("Enter the first exam score: "))
exam2 = float(input("Enter the second exam score: "))

# Calculate the weighted total score
total_score = (exam1 * 0.60) + (exam2 * 0.40)

# Display the total score
print(f"Total Score: {total_score:.2f}")