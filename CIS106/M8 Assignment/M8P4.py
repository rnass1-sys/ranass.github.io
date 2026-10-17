# 1. Create the example data file
item_data = """Widget
10
50
Hammer
2
10
Saw
4
8
"""
with open("orders.txt", "w") as f:
    f.write(item_data)

# 2. Process orders from the text file
total_extended_price = 0.0
order_count = 0

print(f"{'Item':<12}{'Qty':>5}{'Price':>10}{'Ext. Price':>14}")
print("-" * 43)

with open("orders.txt", "r") as file:
    while True:
        item_line = file.readline()
        qty_line = file.readline()
        price_line = file.readline()
        
        if not item_line or not qty_line or not price_line:
            break
            
        item = item_line.strip()
        quantity = int(qty_line.strip())
        price = float(price_line.strip())
        
        # Calculations
        extended_price = quantity * price
        total_extended_price += extended_price
        order_count += 1
        
        print(f"{item:<12}{quantity:>5} ${price:>8,.2f}  ${extended_price:>11,.2f}")

# Calculate average order safely
average_order = total_extended_price / order_count if order_count > 0 else 0.0

print("-" * 43)
print(f"Sum of all extended prices: ${total_extended_price:,.2f}")
print(f"Count of orders:            {order_count}")
print(f"Average order:              ${average_order:,.2f}")
