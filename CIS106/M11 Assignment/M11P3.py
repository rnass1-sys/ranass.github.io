def calculate_commission(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05

    next_year_target = sales * 1.05
    return commission, next_year_target


last_name = input("Enter salesperson's last name: ")
sales = float(input("Enter sales amount: "))

commission, next_year_target = calculate_commission(sales)

print("\nSales Report")
print("Salesperson:", last_name)
print("Commission: $", format(commission, ".2f"))
print("Next Year's Target: $", format(next_year_target, ".2f"))