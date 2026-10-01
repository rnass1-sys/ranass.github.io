# M6P3: CD Interest Rate Calculator

# 1. Get user input
principal = float(input("Enter the principal amount of the CD: $"))
years = int(input("Enter years to maturity: "))

# 2. Determine interest rate using compound conditions inside an else-if hierarchy
if principal > 100000 and years == 5:
    interest_rate = 0.06
elif (principal >= 50000 and principal <= 100000) and years == 10:
    interest_rate = 0.05
elif (principal >= 50000 and principal <= 100000) and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02

# 3. Calculate first year interest
first_year_interest = principal * interest_rate

# 4. Display results with decimals aligned in columns
print("\n--- CD Earnings Report ---")
print(f"{"Principal Amount:":<20} ${principal:>12,.2f}")
print(f"{"Interest Rate:":<20} {interest_rate * 100:>12.1f}%")
print(f"{"First Year Interest:":<20} ${first_year_interest:>12,.2f}")
