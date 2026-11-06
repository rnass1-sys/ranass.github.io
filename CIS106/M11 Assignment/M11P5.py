total = 0
tax = 0

def calculate_total_tax(quantity, unit_price):
    global total
    global tax

    total = quantity * unit_price
    tax = total * 0.07


quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

calculate_total_tax(quantity, unit_price)

print("\nPurchase Report")
print("Total: $", format(total, ".2f"))
print("Tax: $", format(tax, ".2f"))