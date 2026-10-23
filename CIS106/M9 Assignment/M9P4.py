# Problem 4 - Gross Pay

def get_pay_rate(job_code):
    if job_code.upper() == 'L':
        return 25
    elif job_code.upper() == 'A':
        return 30
    elif job_code.upper() == 'J':
        return 50
    else:
        return 0

total_gross_pay = 0

while True:
    lastname = input("Enter employee last name (or STOP to quit): ")

    if lastname.upper() == "STOP":
        break

    job_code = input("Enter job code (L, A, J): ")
    hours = float(input("Enter hours worked: "))

    pay_rate = get_pay_rate(job_code)

    if hours <= 40:
        gross_pay = hours * pay_rate
    else:
        gross_pay = (40 * pay_rate) + ((hours - 40) * pay_rate * 1.5)

    print(f"{lastname}'s Gross Pay: ${gross_pay:.2f}")

    total_gross_pay += gross_pay

print(f"\nTotal Gross Pay: ${total_gross_pay:.2f}")