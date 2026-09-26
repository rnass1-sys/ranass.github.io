# Step 1: Request inputs
num_books = int(input("Enter the number of books to order: "))
cost_per_book = float(input("Enter the cost per book ($): "))

# Step 2: Calculate total order cost
order_total = num_books * cost_per_book

# Step 3: Determine shipping charges based on total cost
if order_total > 50.00:
    shipping_charge = 0.00
else:
    shipping_charge = 25.00

# Step 4: Display the results
print(f"\nOrder Total: ${order_total:.2f}")
print(f"Shipping Charge: ${shipping_charge:.2f}")
