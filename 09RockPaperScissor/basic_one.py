print("Rock...")
print("Paper...")
print("Scissor...")

player_one = input("Player 1, Make your move:")
player_two = input("Player 2, Make your move:")

if player_one == player_two:
    print("Draw")
elif player_one == "rock":
    if player_two == "scissors":
        print("Player 1 WON!")
    elif player_two == "papers":
        print("Palyer 2 WON")
elif player_one == "papers":
    if player_two == "rock":
        print("Palyer 1 WON")
    elif player_two == "scissors":
        print("Palyer 2 WON")
elif player_one == "scissors":
    if player_two == "rock":
        print("Palyer 2 WON")
    elif player_two == "papers":
        print("Palyer 1 WON")
else:
    print("Something Wrong!")