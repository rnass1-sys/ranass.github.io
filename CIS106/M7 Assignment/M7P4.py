# Initialize accumulators and counters
total_gross_pay = 0.0
employee_count = 0

# Initial loop control prompt
run_program = input("Do you want to run this program? (Yes to continue): ")

while run_program.strip().lower() == "yes":
    # Gather inputs
    last_name = input("\nEnter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate of pay: "))
    
    # Compute gross pay with overtime (over 40 hours)
    if hours > 40:
        regular_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours * rate
        
    # Display individual payroll results
    print(f"Employee: {last_name} | Gross Pay: ${gross_pay:.2f}")
    
    # Accumulate summaries
    total_gross_pay += gross_pay
    employee_count += 1
    
    # Bottom prompt to control loop execution
    run_program = input("\nDo you want to enter data for another employee? (Yes to continue): ")

    # Final summaries after the loop ends
    if employee_count > 0:
        average_pay = total_gross_pay / employee_count
        print("\n--- Summary Report ---")
        print(f"Total Gross Pay: ${total_gross_pay:.2f}")
        print(f"Total Employees: {employee_count}")
        print(f"Average Pay: ${average_pay:.2f}")
    else:
        print("\nNo employee data was entered.")