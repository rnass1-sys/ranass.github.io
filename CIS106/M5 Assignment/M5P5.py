# Step 1: Input taxpayer data
last_name = input("Enter the user's last name: ")
num_dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter the gross income ($): "))

# Step 2: Compute adjusted gross income (AGI)
adjusted_gross_income = gross_income - (num_dependents * 12000)

# Step 3: Determine tax rate based on AGI tier
if adjusted_gross_income > 50000.00:
    tax_rate = 0.20
else:
    tax_rate = 0.10

# Step 4: Compute initial income tax
income_tax = adjusted_gross_income * tax_rate

# Step 5: Adjust for safety net floor if income tax drops below zero
if income_tax < 0:
    income_tax = 100.00

# Step 6: Display the results
print(f"\nLast Name: {last_name}")
print(f"Gross Income: ${gross_income:,.2f}")
print(f"Number of Dependents: {num_dependents}")
print(f"Adjusted Gross Income: ${adjusted_gross_income:,.2f}")
print(f"Income Tax: ${income_tax:,.2f}")
