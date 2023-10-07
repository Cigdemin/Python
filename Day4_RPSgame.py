rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_choice = input("What do you chose. Type 0 for Rock, 1 for Paper and 2 for the Scissors. \n "
)
if int(player_choice) >= 3 :
  print("You write a not valid number,try again!")
else:
  if int(player_choice) == 0:
      print("You choose\n" + rock)
  if int(player_choice) == 1:
      print("You choose\n" + paper)
  if int(player_choice) == 2:
      print("You choose\n" + scissors)
  
  computer_choice = random.randint(0, 2)
  if computer_choice == 0:
      print("Computer choose\n" + rock)
  if computer_choice == 1:
      print("Computer choose\n" + paper)
  if computer_choice == 2:
      print("Computer choose\n" + scissors)
  # Rock wins against scissors.
  # Scissors win against paper.
  # Paper wins against rock.
  result = str(player_choice) + str(computer_choice)
  #print(result)
  winning_result = ["02", "10", "12", "21"]
  loosing_results = ["01", "20"]
  if result in winning_result:
      print("your win!")
  elif result in loosing_results:
      print("you lost")
  else:
      print("No winner/looser,you chose the same. Play again!")
  