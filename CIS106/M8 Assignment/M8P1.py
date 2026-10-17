# Prompt user for inputs
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))

print("\nFormatted output\n")
# Print table headers with alignment matching the example
print(f"{'Year':<5}{'Beginning':>12}{'Ending':>12}")
print(f"{'':<5}{'Balance':>12}{'Balance':>12}")

total_interest = 0.0

# Run a loop for the first 5 years
for year in range(1, 6):
    beginning_balance = principal
    interest = beginning_balance * rate
    ending_balance = beginning_balance + interest
    
    # Update cumulative totals and the principal for the next iteration
    total_interest += interest
    principal = ending_balance
    
    # Display year stats with currency formatting
    print(f"{year:<5} ${beginning_balance:,.2f} ${ending_balance:,.2f}")

# Display the total accumulated interest
print(f"\nTotal interest earned: ${total_interest:,.2f}")