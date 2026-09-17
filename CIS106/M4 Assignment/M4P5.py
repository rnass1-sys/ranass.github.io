# Problem 5: Business Break-Even Point Calculator

# Get financial entries from the user
fixed_costs = float(input("Enter fixed costs: "))
price_per_unit = float(input("Enter price per unit: "))
cost_per_unit = float(input("Enter cost per unit: "))

# Compute the break-even point
# Break-even = fixed costs / (price per unit - cost per unit)
break_even_point = fixed_costs / (price_per_unit - cost_per_unit)

# Display break-even point
print(f"Break-Even Point: {break_even_point:.2f} units")
