import os

def print_batting_averages(players_dict):
    """Prints player names and batting averages in two formatted columns."""
    print(f"{'Player Name':<15} {'Batting Average':>16}")
    print("-" * 32)
    for name, average in players_dict.items():
        print(f"{name:<15} {average:>16.3f}")

# Automatically locate batting_averages.txt in the same folder as M13P3.py
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "batting_averages.txt")

# Load data from the text file into a dictionary
batting_dict = {}

with open(file_path, "r") as file:
    for line in file:
        if line.strip():
            name, avg = line.strip().split()
            batting_dict[name] = float(avg)

# Call the function to display the contents
print_batting_averages(batting_dict)
