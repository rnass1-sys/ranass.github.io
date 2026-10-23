# Problem 1 - Extended Price with Function

def compute_total(quantity, price):
    total = quantity * price

    # Apply 10% discount if over $10,000
    if total > 10000:
        total = total * 0.90

    return total


total_extended_price = 0

while True:
    signal = input("Enter 'Y' to continue or 'N' to stop: ").upper()

    if signal == 'N':
        break

    qty = float(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    ext_price = compute_total(qty, price)

    print("\nItem Information")
    print("----------------")
    print(f"Quantity: {qty}")
    print(f"Price: ${price:.2f}")
    print(f"Extended Price: ${ext_price:.2f}\n")

    total_extended_price += ext_price

print("--------------------------------")
print(f"Total Extended Price: ${total_extended_price:.2f}")