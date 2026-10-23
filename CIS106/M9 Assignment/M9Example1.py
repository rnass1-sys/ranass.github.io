# Example 1 - Rewards Points

def compute_rewards(points, code):
    if code.upper() == 'C':
        return points * 2
    elif code.upper() == 'X':
        return points * 3
    else:
        return points * 1.5

while True:
    points = input("Enter points (or STOP to quit): ")

    if points.upper() == "STOP":
        break

    points = int(points)
    code = input("Enter redemption code: ")

    rewards = compute_rewards(points, code)

    print(f"Points: {points}")
    print(f"Code: {code}")
    print(f"Rewards Points: {rewards}")