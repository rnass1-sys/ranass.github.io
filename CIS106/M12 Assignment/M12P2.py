last_names = [
    "Smith", "Jones", "Brown", "Davis", "Wilson",
    "Moore", "Taylor", "Clark", "Hall", "Young"
]

scores = [88, 92, 75, 84, 96, 78, 91, 85, 89, 73]

def display_students(names, scores):
    print("Names and Scores:")
    for i in range(len(names)):
        print(names[i], scores[i])

def display_students_reverse(names, scores):
    print("\nNames and Scores in Reverse Order:")
    for i in range(len(names) - 1, -1, -1):
        print(names[i], scores[i])

display_students(last_names, scores)
display_students_reverse(last_names, scores)