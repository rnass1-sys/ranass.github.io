import os

player_names = []
batting_averages = []

def load_file():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "players.txt")
    file = open(file_path, "r")

    for line in file:
        if line.strip() != "":
            data = line.strip().split(",")
            player_names.append(data[0].strip())
            batting_averages.append(float(data[1].strip()))

    file.close()

def display_players():
    print("Players and Batting Averages")
    for i in range(len(player_names)):
        print(player_names[i], batting_averages[i])

def search_player(name):
    found = False

    for i in range(len(player_names)):
        if player_names[i].lower() == name.lower():
            print("Found:")
            print(player_names[i], batting_averages[i])
            found = True
            break

    if not found:
        print("Name not found")

load_file()
display_players()

while True:
    search_name = input("\nEnter player last name (or QUIT): ")

    if search_name.upper() == "QUIT":
        break

    search_player(search_name)
