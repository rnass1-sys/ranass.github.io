# Counter for students
student_count = 0

# Initial loop control prompt
run_program = input("Do you want to run this program? (Yes to continue): ")

while run_program.strip().lower() == "yes":
    # Gather inputs
    last_name = input("\nEnter student's last name: ")
    score1 = float(input("Enter first exam score: "))
    score2 = float(input("Enter second exam score: "))
    
    # Compute average
    average = (score1 + score2) / 2
    
    # Display student results
    print(f"Student: {last_name} | Average Score: {average:.2f}")
    
    # Increment student counter
    student_count += 1
    
    # Bottom prompt to control loop execution
    run_program = input("\nDo you want to enter data for another student? (Yes to continue): ")

    # Final summary after the loop
    print(f"\nTotal number of students entered: {student_count}")