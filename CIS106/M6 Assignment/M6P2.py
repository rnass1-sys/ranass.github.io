# M6P2: Part Cost Calculator

# 1. Get user input
part_number = input("Enter part number: ").strip()
quantity = int(input("Enter quantity: "))

# 2. Determine unit cost using structured else-if chains
if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00

# 3. Calculate total cost
total_cost = quantity * unit_cost

# 4. Display results with decimals aligned in columns
print("\n--- Order Summary ---")
print(f"{"Part Number:":<20} {part_number:>13}")
print(f"{"Cost per Unit:":<20} ${unit_cost:>12,.2f}")
print(f"{"Total Cost:":<20} ${total_cost:>12,.2f}")
