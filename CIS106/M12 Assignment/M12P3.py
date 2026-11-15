last_names = [
    "Smith", "Jones", "Brown", "Davis", "Wilson",
    "Moore", "Taylor", "Clark", "Hall", "Young"
]

scores = [88, 92, 75, 84, 96, 78, 91, 85, 89, 73]

def display_data(names, scores):
    print("Student Scores:")
    for i in range(len(names)):
        print(names[i], scores[i])

def find_highest(names, scores):
    high_var = 0
    high_index = 0

    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i

    print("\nHighest Score:")
    print(names[high_index], high_var)

def find_lowest(names, scores):
    low_var = 999
    low_index = 0

    for i in range(len(scores)):
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print("\nLowest Score:")
    print(names[low_index], low_var)

display_data(last_names, scores)
find_highest(last_names, scores)
find_lowest(last_names, scores)