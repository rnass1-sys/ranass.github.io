# Step 1: Request user input
item = input("Enter the item (A or B): ").strip().upper()
quantity = int(input("Enter the quantity: "))

# Step 2: Determine unit price using relational condition only for A
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

# Step 3: Compute extended price
extended_price = quantity * unit_price

# Step 4: Display the results
print(f"\nItem: {item}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")
