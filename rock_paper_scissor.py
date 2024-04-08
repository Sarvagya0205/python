import random

def get_choices():
    player_choice=input("Enter a choice ( rock, paper , scissor):")
    options = ["rock", "paper" , "scissor"]
    computer_choice= random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices


def check_win(player , computer):
 print(f"You chose {player} , computer chose {computer}") 
 if player == computer:
     return "It's a tie!"
 elif player == "rock":
      if computer == "scissor":
          return "Rock smashes scissors! You Win!"
      elif computer == "paper":
          return "Paper covers rock! you lose."
 elif player == "paper":
      if computer == "scissor":
          return "Scissor cuts paper! You Lose!"
      elif computer == "rock":
          return "Paper covers rock! You Win !"
 elif player== "scissor":
      if computer == "rock":
         return "Rock smashes scissors! You Lose!"
      elif computer == "paper":
         return "Scissor cuts paper ! You Win."
    
#     #using fstring 
# age = 25 
# print(f"jim is {age} years old")

choices=get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
  





     

