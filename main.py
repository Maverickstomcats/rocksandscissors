import random 

choices = ["rock","paper","scissors"]
player = None
  
computer = random.choice(choices)
while player not in choices:
    player = input("rock, paper or scissors?:") 
  
if player == computer:
    print("computer:", computer)
    print("player:",player)
    print("tie!")
elif player == "rock":
    if computer == "paper":
      print("computer:", computer)
      print("player:",player)
      print("you lose!! :(")
    if computer == "scissors":
      print("computer:", computer)
      print("player:",player)
      print("you win!! :)")
elif player == "paper":
    if computer == "rock":
      print("computer:", computer)
      print("player:",player)
      print("you win!! :)")
    if computer == "scissors":
      print("computer:", computer)
      print("player:",player)
      print("you lose!! :(")
elif player == "scissors":
    if computer == "paper":
      print("computer:", computer)
      print("player:",player)
      print("you win!! :)")
    if computer == "rock":
      print("computer:", computer)
      print("player:",player)
      print("you lose!! :(")
   