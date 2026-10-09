# Initialize total discount counter
total_discounts_sum = 0.0

# Initial loop control prompt
run_program = input("Do you want to run this program? (Yes to continue): ")

while run_program.strip().lower() == "yes":
    # Gather inputs
    quantity = int(input("\nEnter item quantity: "))
    price = float(input("Enter item price: "))
    
    # Compute extended price
    extended_price = quantity * price
    
    # Determine discount rate
    if extended_price > 10000.00:
        discount_percent = 0.25
    else:
        discount_percent = 0.10
        
    # Calculate discount amount and order total
    discount_amount = extended_price * discount_percent
    order_total = extended_price - discount_amount
    
    # Display individual order results
    print(f"\nOrder Details:")
    print(f"  Extended Price:  ${extended_price:.2f}")
    print(f"  Discount Amount: ${discount_amount:.2f} ({discount_percent*100:.0f}%)")
    print(f"  Total Due:       ${order_total:.2f}")
    
    # Add to total discounts tracker
    total_discounts_sum += discount_amount
    
    # Bottom prompt to control loop execution
    run_program = input("\nDo you want to enter another order? (Yes to continue): ")

    # Final summary after the loop ends
    print("\n--- Final Report ---")
    print(f"Sum of all discounts given: ${total_discounts_sum:.2f}")
