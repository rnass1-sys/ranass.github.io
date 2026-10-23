# Problem 5 - Tuition Owed

def compute_tuition(credit_hours, district_code):
    if district_code.upper() == 'I':
        rate = 250
    elif district_code.upper() == 'O':
        rate = 550
    else:
        rate = 0

    return credit_hours * rate

total_tuition = 0

while True:
    lastname = input("Enter student last name (or STOP to quit): ")

    if lastname.upper() == "STOP":
        break

    credit_hours = int(input("Enter credit hours: "))
    district_code = input("Enter district code (I/O): ")

    tuition = compute_tuition(credit_hours, district_code)

    print(f"{lastname}'s Tuition Owed: ${tuition:.2f}")

    total_tuition += tuition

print(f"\nTotal Tuition Owed: ${total_tuition:.2f}")