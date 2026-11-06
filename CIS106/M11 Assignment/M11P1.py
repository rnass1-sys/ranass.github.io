def calculate_discount(quantity, price, discount_rate):
    total = quantity * price
    discount_amount = total * (discount_rate / 100)
    discounted_price = total - discount_amount
    return discount_amount, discounted_price

quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate (%): "))

discount_amount, discounted_price = calculate_discount(
    quantity, price, discount_rate
)

print("\nSales Report")
print("Quantity:", quantity)
print("Price: $", format(price, ".2f"))
print("Discount Amount: $", format(discount_amount, ".2f"))
print("Discounted Price: $", format(discounted_price, ".2f"))