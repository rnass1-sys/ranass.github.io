def compute_assessed_value(county, market_value):
    county = county.lower()

    if county == "cook":
        percent = 0.90
    elif county == "dupage":
        percent = 0.80
    elif county == "mchenry":
        percent = 0.75
    elif county == "kane":
        percent = 0.60
    else:
        percent = 0.70

    return market_value * percent


total_market_value = 0
total_assessed_value = 0

while input("Do you want to enter data? (Yes/No): ").lower() == "yes":
    county = input("County: ")
    market_value = float(input("Market Value: "))

    assessed_value = compute_assessed_value(county, market_value)

    total_market_value += market_value
    total_assessed_value += assessed_value

    print(f"Assessed Value: ${assessed_value:.2f}\n")

print(f"\nTotal Market Value: ${total_market_value:.2f}")
print(f"Total Assessed Value: ${total_assessed_value:.2f}")