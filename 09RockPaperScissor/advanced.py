import random

print("Rock...")
print("Paper...")
print("Scissor...")

options = ["rock", "papers", "scissors"]
print("Enter Your Move:")
me = input()

rand = random.randint(0, 2)
pc = options[rand]

player_one = me
player_two = pc

print(f"You Choose: {me}, PC choose {pc}")

if player_one == player_two:
    print("Draw")
elif player_one == "rock":
    if player_two == "scissors":
        print("You WON!")
    elif player_two == "papers":
        print("PC WON!")
elif player_one == "papers":
    if player_two == "rock":
        print("You WON!")
    elif player_two == "scissors":
        print("PC WON!")
elif player_one == "scissors":
    if player_two == "rock":
        print("PC WON!")
    elif player_two == "papers":
        print("You WON")
else:
    print("Something Wrong!")