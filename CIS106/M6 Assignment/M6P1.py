# M6P1: Widget Price Calculator

# 1. Get user input
quantity = int(input("Enter quantity of widgets: "))

# 2. Determine price per widget using explicit else-if checks
if quantity > 10000:
    price = 10.00
elif quantity >= 5000 and quantity <= 10000:  # 5000 to 10000
    price = 20.00
else:                                          # Below 5000
    price = 30.00

# 3. Perform calculations
extended_price = quantity * price
tax_amount = extended_price * 0.07
total_cost = extended_price + tax_amount

# 4. Display results with decimals aligned in columns
print("\n--- Invoice Summary ---")
print(f"{"Extended Price:":<20} ${extended_price:>12,.2f}")
print(f"{"Tax Amount (7%):":<20} ${tax_amount:>12,.2f}")
print(f"{"Total:":<20} ${total_cost:>12,.2f}")
