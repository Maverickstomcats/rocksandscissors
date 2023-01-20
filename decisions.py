import random 
import choices
 
player = None 
def computers(choices):
  computer = random.choice(choices)
  return computer

def players(choices,player):
  while player not in choices:
    player = input("rock, paper or scissors?:")
    return player