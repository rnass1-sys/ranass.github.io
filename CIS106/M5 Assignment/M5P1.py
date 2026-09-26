# Step 1: Input the quantity
quantity = int(input("Enter the quantity of the item: "))

# Step 2: Determine the unit price
if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

# Step 3: Compute extended price
extended_price = quantity * unit_price

# Step 4: Compute tax (7%)
tax = extended_price * 0.07

# Step 5: Compute total
total = extended_price + tax

# Step 6: Display the results
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
