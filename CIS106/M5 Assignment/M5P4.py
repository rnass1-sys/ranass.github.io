# Step 1: Get appliance details
appliance_name = input("Enter the name of the appliance: ")
appliance_cost = float(input("Enter the cost of the appliance ($): "))

# Step 2: Determine warranty percentage based on cost threshold
if appliance_cost > 1000.00:
    warranty_rate = 0.10
else:
    warranty_rate = 0.05

# Step 3: Calculate warranty fees and final total cost
warranty_cost = appliance_cost * warranty_rate
total_cost = appliance_cost + warranty_cost

# Step 4: Display the results
print(f"\nAppliance Name: {appliance_name}")
print(f"Appliance Cost: ${appliance_cost:,.2f}")
print(f"Warranty Cost: ${warranty_cost:,.2f}")
print(f"Total Cost: ${total_cost:,.2f}")
