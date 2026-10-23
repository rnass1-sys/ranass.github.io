# Problem 2 - Batting Average

def compute_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats

player_count = 0

while True:
    lastname = input("Enter player's last name (or STOP to quit): ")

    if lastname.upper() == "STOP":
        break

    hits = int(input("Enter hits: "))
    at_bats = int(input("Enter at bats: "))

    average = compute_batting_average(hits, at_bats)

    print(f"{lastname}'s batting average: {average:.3f}")

    player_count += 1

print(f"\nTotal players entered: {player_count}")