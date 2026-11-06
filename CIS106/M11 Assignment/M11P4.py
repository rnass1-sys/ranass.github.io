def calculate_bowling_average(score1, score2, score3, handicap):
    average_score = (score1 + score2 + score3) / 3
    average_with_handicap = average_score + handicap
    return average_score, average_with_handicap


last_name = input("Enter bowler's last name: ")

score1 = int(input("Enter game score 1: "))
score2 = int(input("Enter game score 2: "))
score3 = int(input("Enter game score 3: "))
handicap = int(input("Enter handicap: "))

average_score, average_with_handicap = calculate_bowling_average(
    score1, score2, score3, handicap
)

print("\nBowling Report")
print("Bowler:", last_name)
print("Average Score:", format(average_score, ".2f"))
print("Average Score with Handicap:", format(average_with_handicap, ".2f"))