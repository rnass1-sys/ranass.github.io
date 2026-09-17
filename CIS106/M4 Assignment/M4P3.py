# Problem 3: Meal Tip Calculator with specific layout formatting

# Get total cost of the meal from the user
meal_total = float(input("Enter the total for the meal: "))

# Define tip percentages
tips = [0.15, 0.18, 0.20]

# Loop through percentages and display in exact 9-line structure with required blank lines
for i, tip_pct in enumerate(tips):
    tip_value = meal_total * tip_pct
    total_with_tip = meal_total + tip_value
    
    print(f"With {int(tip_pct * 100)}% Tip:")
    # Using 10-character width for aligned alignment like the class examples
    print(f"Total:         {meal_total:10.2f}")
    print(f"Tip:           {tip_value:10.2f}")
    print(f"Total with Tip {total_with_tip:10.2f}")
    
    # Print a blank line between tip sets, but not after the last one
    if i < len(tips) - 1:
        print()
