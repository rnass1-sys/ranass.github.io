last_names = [
    "Smith", "Jones", "Brown", "Davis", "Wilson",
    "Moore", "Taylor", "Clark", "Hall", "Young"
]

def display_names(names):
    print("Names in order:")
    for name in names:
        print(name)

def display_names_reverse(names):
    print("\nNames in reverse order:")
    for i in range(len(names) - 1, -1, -1):
        print(names[i])

display_names(last_names)
display_names_reverse(last_names)