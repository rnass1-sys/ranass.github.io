def compute_price(msrp, make, model, electric_code):
    make = make.lower()
    model = model.lower()
    electric_code = electric_code.upper()

    if make == "honda" and model == "accord":
        discount_percent = 0.10
    elif make == "toyota" and model == "rav4":
        discount_percent = 0.15
    elif electric_code == "Y":
        discount_percent = 0.30
    else:
        discount_percent = 0.05

    discount = msrp * discount_percent
    sale_price = msrp - discount
    total_price = sale_price * 1.07

    return total_price


total_msrp = 0
total_sales_price = 0

while input("Do you want to enter data? (Yes/No): ").lower() == "yes":
    make = input("Make: ")
    model = input("Model: ")
    electric_code = input("Electric Vehicle (Y/N): ")
    msrp = float(input("MSRP: "))

    out_door_price = compute_price(msrp, make, model, electric_code)

    total_msrp += msrp
    total_sales_price += out_door_price

    print(f"Out-the-Door Price: ${out_door_price:.2f}\n")

print(f"\nTotal MSRP: ${total_msrp:.2f}")
print(f"Total Sales Price: ${total_sales_price:.2f}")