from decisions import computers, players
from process import gamefunction
choices = ["rock","paper","scissors"]




#OG code
# import random 
# while True:
#   choices = ["rock","paper","scissors"]
#   player = None
   
#   computer = random.choice(choices)
#   while player not in choices:
#       player = input("rock, paper or scissors?:") 
#     #can i convert lines 10 to 40 to a function? 
#   if player == computer:
#       print("computer:", computer)
#       print("player:",player)
#       print("tie!")
#   elif player == "rock":
#       if computer == "paper":
#         print("computer:", computer)
#         print("player:",player)
#         print("you lose!! :(")
#       if computer == "scissors":
#         print("computer:", computer)
#         print("player:",player)
#         print("you win!! :)")
#   elif player == "paper":
#       if computer == "rock":
#         print("computer:", computer)
#         print("player:",player)
#         print("you win!! :)")
#       if computer == "scissors":
#         print("computer:", computer)
#         print("player:",player)
#         print("you lose!! :(")
#   elif player == "scissors":
#       if computer == "paper":
#         print("computer:", computer)
#         print("player:",player)
#         print("you win!! :)")
#       if computer == "rock":
#         print("computer:", computer)
#         print("player:",player)
#         print("you lose!! :(")

#   play_again = input("do you want to play again? (y/n)")
#   if play_again != "yes":
#     print("BAAAAAAAAAIIIIIIIIII :)")