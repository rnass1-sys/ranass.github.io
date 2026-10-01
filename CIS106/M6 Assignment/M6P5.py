# M6P5: Employee Bonus Calculator

# 1. Get user input
last_name = input("Enter employee last name: ").strip()
salary = float(input("Enter employee salary: $"))
job_level = int(input("Enter job level: "))

# 2. Determine bonus rate based on explicit job level boundaries
if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5 and job_level <= 9:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

# 3. Compute bonus amount
bonus_amount = salary * bonus_rate

# 4. Display results with decimals aligned in columns
print("\n--- Bonus Statement ---")
print(f"{"Employee Last Name:":<20} {last_name:>13}")
print(f"{"Base Salary:":<20} ${salary:>12,.2f}")
print(f"{"Bonus Rate:":<20} {bonus_rate * 100:>12.1f}%")
print(f"{"Calculated Bonus:":<20} ${bonus_amount:>12,.2f}")
