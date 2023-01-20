from decisions import computerchoices, playerschoice
import choices
def gamefunction(choices,computers,players):
  if players == computers:
    print("computer:", computers)
    print("player:",players)
    print("tie!")
  elif players == "rock":
    if computers == "paper":
      print("computer:", computers)
      print("player:",players)
      print("you lose!! :(")
    if computers == "scissors":
      print("computer:", computers)
      print("player:",players)
      print("you win!! :)")
  elif players == "paper":
    if computers == "rock":
      print("computer:", computers)
      print("player:",players)
      print("you win!! :)")
    if computers == "scissors":
      print("computer:", computers)
      print("player:",players)
      print("you lose!! :(")
  elif players == "scissors":
    if computers == "paper":
      print("computer:", computers)
      print("player:",players)
      print("you win!! :)")
    if computers == "rock":
      print("computer:", computers)
      print("player:",players)
      print("you lose!! :(")
   