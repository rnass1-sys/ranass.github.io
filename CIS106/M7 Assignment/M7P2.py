# Get inputs from the user
start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
increment = int(input("Enter the increment value: "))

current = start

# Loop from start to stop value
while current <= stop:
    print(current)
    current += increment