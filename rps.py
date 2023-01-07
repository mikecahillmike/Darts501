import random
rps = ["Rock", "Paper", "Scissors"]
player = False
while True:
    computer = random.choice(rps)
    player = input("Choose: rock, paper or  scissors!   ").capitalize()
    # check for draw
    if player == computer:
        print("Draw!")

    # if you chose rock
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)

    # if you chose paper
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)

    # if you chose scissors
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    break