# Problem 4: Step and Calories Burned Calculator

# Get name and steps walked from the user
first_name = input("Enter first name: ")
steps = int(input("Enter number of steps walked: "))

# Compute calories burned (.25 calories per step)
calories_burned = steps * 0.25

# Display first name and calories burned
print(f"First Name: {first_name}")
print(f"Calories Burned: {calories_burned:.2f}")
