def compute_forecast(month, sales):
    month = month.lower()

    if month in ["Jan", "Feb", "Mar"]:
        percent = 0.10
    elif month in ["Apr", "May", "Jun"]:
        percent = 0.15
    elif month in ["Jul", "Aug", "Sep"]:
        percent = 0.20
    else:
        percent = 0.25

    return sales * (1 + percent)


while input("Do you want to enter data? (Yes/No): ").lower() == "yes":
    last_name = input("Enter last name: ")
    month = input("Enter month (Jan-Dec): ")
    sales = float(input("Enter sales amount: "))

    forecast_sales = compute_forecast(month, sales)

    print(f"\nEmployee: {last_name}")
    print(f"Next Month Forecast: ${forecast_sales:.2f}\n")