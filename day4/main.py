import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

filename = "input.txt"
if not os.path.isabs(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)

with open(filename) as f:
    lines = f.read().splitlines()
    
players = {}
for line in lines:
    player, numbers = line.split(":")
    player = player.strip()
    numbers = numbers.strip()
    numbers = numbers.split("|")
    winning_numbers = numbers[0].strip()
    winning_numbers = winning_numbers.split(" ")
    winning_numbers = [int(n) for n in winning_numbers if n.isdigit()]
    player_numbers = numbers[1].strip()
    player_numbers = player_numbers.split(" ")
    player_numbers = [int(n) for n in player_numbers if n.isdigit()]
    players[player] = {"winning_numbers": winning_numbers, "player_numbers": player_numbers}

for player, numbers in players.items():
    winning_numbers = numbers["winning_numbers"]
    player_numbers = numbers["player_numbers"]
    score = 0
    matching_numbers = []
    for player_number in player_numbers:
        if player_number in winning_numbers:
            matching_numbers.append(player_number)
            score = 1
    
    for number in matching_numbers[1:]:
        score *= 2

    
    players[player]["score"] = score

total_score = 0

for player, numbers in players.items():
    total_score += numbers["score"]

print(total_score)
    

    
