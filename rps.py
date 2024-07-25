import random



while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)



    player = None


    while player not in choices:
         player = input("Enter Any One :Rock , paper, scissors :")



    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie")



    elif player == "rock":

       if computer == "paper":
           print("computer: ", computer)
           print("player: ", player)
           print("you have failed")
       if computer == "scissors":

           print("computer: ", computer)
           print("player: ", player)
           print("you have failed")



    elif player == "paper":
       if computer == "rock":
           print("computer: ", computer)
           print("player: ", player)
           print("you have failed")

       if computer == "scissors":
           print("computer: ", computer)
           print("player: ", player)
           print("you won")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you have failed")
        if computer == "paper":
           print("computer: ", computer)
           print("player: ", player)
           print("you have won")
    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you have won")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("you have won")



    a = input("do you to play again ? : yes or no : ")

    if a !="yes":
        break










