# Problem 3 - Miles Per Gallon

def compute_mpg(miles, gallons):
    if gallons == 0:
        return 0
    return miles / gallons

trip_count = 0

while True:
    destination = input("Enter destination city (or STOP to quit): ")

    if destination.upper() == "STOP":
        break

    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))

    mpg = compute_mpg(miles, gallons)

    print("\nTrip Information")
    print(f"Destination: {destination}")
    print(f"Miles: {miles}")
    print(f"MPG: {mpg:.2f}")

    trip_count += 1

print(f"\nNumber of trips entered: {trip_count}")