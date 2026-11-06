def calculate_scores(score1, score2, score3):
    total = score1 + score2 + score3
    average = total / 3
    return total, average


last_name = input("Enter student's last name: ")

score1 = float(input("Enter exam score 1: "))
score2 = float(input("Enter exam score 2: "))
score3 = float(input("Enter exam score 3: "))

total, average = calculate_scores(score1, score2, score3)

print("\nStudent Report")
print("Last Name:", last_name)
print("Total Points:", total)
print("Average Score:", format(average, ".2f"))