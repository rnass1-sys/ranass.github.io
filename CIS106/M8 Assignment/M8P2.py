# Initialize the first two terms starting with 1 as instructed
a, b = 1, 1

print("The first 20 numbers in the Fibonacci sequence:")

# Use a for loop to calculate and display the sequence
for i in range(20):
    print(a, end=", " if i < 19 else "\n")
    # Compute the next number in the sequence
    a, b = b, a + b
