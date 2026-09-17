# Problem 2: Stock Value Change Calculator

# Get stock details from the user
purchase_price = float(input("Enter the purchase price per share: "))
current_price = float(input("Enter the current stock price: "))
quantity = int(input("Enter the quantity of stock: "))

# Compute the value increase or decrease
value_change = (current_price - purchase_price) * quantity

# Display the result
print(f"Stock value change: {value_change:.2f}")