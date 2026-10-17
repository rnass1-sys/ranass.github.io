# 1. Create the example student file
student_data = """Jones
I
12
Adams
I
10
Baker
O
12
Smith
O
16
"""
with open("students.txt", "w") as f:
    f.write(student_data)

# 2. Process tuition statements
total_tuition = 0.0
student_count = 0

print(f"{'Last Name':<12}{'Credits':>8}{'Tuition Owed':>15}")
print("-" * 37)

with open("students.txt", "r") as file:
    while True:
        name_line = file.readline()
        district_line = file.readline()
        credits_line = file.readline()
        
        if not name_line or not district_line or not credits_line:
            break
            
        last_name = name_line.strip()
        district_code = district_line.strip().upper()
        credits = int(credits_line.strip())
        
        # Evaluate credit costs based on code rules
        cost_per_credit = 250.00 if district_code == 'I' else 500.00
        
        tuition_owed = credits * cost_per_credit
        total_tuition += tuition_owed
        student_count += 1
        
        print(f"{last_name:<12}{credits:>8}   ${tuition_owed:>11,.2f}")

print("-" * 37)
print(f"Sum of all tuition owed: ${total_tuition:,.2f}")
print(f"Number of students:       {student_count}")
