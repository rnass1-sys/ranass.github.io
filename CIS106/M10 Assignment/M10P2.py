def wall_square_footage(length, width, height):
    return (2 * length * height) + (2 * width * height)

def floor_ceiling_area(length, width):
    return length * width

while input("Do you want to enter data? (Yes/No): ").lower() == "yes":
    length = float(input("Length: "))
    width = float(input("Width: "))
    height = float(input("Height: "))

    wall_area = wall_square_footage(length, width, height)
    wall_gallons = wall_area / 50

    ceiling_area = floor_ceiling_area(length, width)
    ceiling_gallons = ceiling_area / 50

    print(f"\nWall Square Footage: {wall_area:.2f}")
    print(f"Gallons Needed for Walls: {wall_gallons:.2f}")

    print(f"Ceiling/Floor Area: {ceiling_area:.2f}")
    print(f"Gallons Needed for Ceiling/Floor: {ceiling_gallons:.2f}\n")