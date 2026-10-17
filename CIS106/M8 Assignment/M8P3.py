# 1. Create a sample text file with at least 5 employees as instructed
sample_data = """Adams
50000.00
Baker
75000.00
Smith
45000.00
Jones
120000.00
Davis
30000.00
"""
with open("employees.txt", "w") as f:
    f.write(sample_data)

# 2. Read and process the data file
total_bonuses_paid = 0.0

print(f"{'Last Name':<12}{'Salary':>12}{'Bonus':>12}")
print("-" * 38)

with open("employees.txt", "r") as file:
    while True:
        # Read the next two lines (name and salary)
        name_line = file.readline()
        salary_line = file.readline()
        
        # Break the loop if we hit the end of the file
        if not name_line or not salary_line:
            break
            
        last_name = name_line.strip()
        salary = float(salary_line.strip())
        
        # Determine the bonus rate bracket
        if salary >= 100000.00:
            rate = 0.20
        elif salary >= 50000.00:
            rate = 0.15
        else:
            rate = 0.10
            
        # Compute individual stats
        bonus = salary * rate
        total_bonuses_paid += bonus
        
        print(f"{last_name:<12}${salary:>11,.2f}${bonus:>11,.2f}")

        print("-" * 38)
        print(f"Sum of all bonuses paid out: ${total_bonuses_paid:,.2f}")
