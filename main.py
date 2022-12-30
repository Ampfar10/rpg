import random

# Set up the players
players = ["player1", "player2"]
health = [100, 100]
points = [0, 0]

# Create a list of weapon names and damages
weapons = [("pistol", 10, 20), ("rifle", 15, 25), ("sniper", 20, 30)]

# Main game loop
while True:
    # Choose a random player to attack
    attacker = random.choice(players)
    index = players.index(attacker)

    # Choose a random player to be attack
    defender = players[index - 1]
    defender_index = players[index - 1]

    # Ask the attacker to choose a weapon
    print(f"{attacker}, choose a weapon:")
    for i, weapon in enumerate(weapons):
        print(f"{i + 1}: {weapon[0]}")
    choice = int(input())
    weapon_name, min_damage, max_damage = weapons[choice - 1]

    # Calculate the damage
    damage = random.randint(min_damage, max_damage)

    # Subtract the damage from the defender's health
    health[defender_index] -= damage

    # Print the attack message
    print(f"{attacker} shoots {defender} with a {weapon_name} for {damage} damage!")

    # Check if the game is over
    if health[0] <= 0 or health[1] <= 0:
        break

# Determine the winner based on the amount of damage dealt
if health[0] == health[1]:
    print("It's a tie!")
elif health[0] > health[1]:
    print("Player 1 wins!")
    points[0] += 30
else:
    print("Player 2 wins!")
    points[1] += 30

# Print the final scores
print(f"Player 1: {points[0]} points")
print(f"Player 2: {points[1]} points")
