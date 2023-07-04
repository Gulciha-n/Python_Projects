import random

action_list = ["rock","paper","scissors"]

computer_score=0
player_score=0

total_rounds=input("How many rounds do you want play? Please enter a number :")
round_counter = 0

while True:
  round_counter += 1
  print("Round number :",round_counter)
  computer_choice = random.choice(action_list)
  player_choice = input("Please choice your action:")

  print("player choice :",player_choice)
  print("Computer choice :",computer_choice)


  if computer_choice == player_choice:
    print("Both player chose the same action.")  

  elif computer_choice == "paper":
    if player_choice == "rock":
      print("Winner is : computer!")
      computer_score += 1
    else:
      print("Winner is :player!")
      player_score +=1

  elif computer_choice == "rock":
    if player_choice == "paper":
      print("Winner is : player!")
      player_score +=1
    else:
      print("Winner is : computer!")
      computer_score += 1

  elif computer_choice == "scissors":
    if player_choice == "rock":
      print("Winner is : player!")
      player_score +=1
    else:
      print("Winner is : computer!")
      computer_score += 1

  if round_counter == int(total_rounds):
    break

if computer_score == player_score:
  print ("There is no winner, tie.",computer_score,":",player_score)
elif computer_score > player_score:
  print("Computer won ",computer_score,":",player_score)
elif player_choice < player_score:
  print("Player won",computer_score,":",player_score)
