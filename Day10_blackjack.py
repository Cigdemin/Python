
from blackjack_art import logo
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_number1 = random.choice(cards)
user_number2 = random.choice(cards)
user_hand = [user_number1, user_number2]
user_current_score = sum(user_hand)

comp_number1 = random.choice(cards)
comp_number2 = random.choice(cards)
comp_hand = [comp_number1, comp_number2]
comp_current_score = sum(comp_hand)
play_again = True
response = input("Do you want to play a Balckjack game? Type 'y' or 'n': ")
if "y" in response:
    print(f"{logo}")
    print(f"Your cards: {user_hand} and current score: {user_current_score}")
    print(f"Computer`s first card [{comp_number1}]")
    adding_card = input("Type 'y' to get another card or type 'n' to pass: ")
    play_again = True
    if "y" in adding_card :
      play_again == True
    if "n" in adding_card :
      play_again == False
    while play_again == True :
        user_number = random.choice(cards)
        comp_number = random.choice(cards)
        if user_number == 11 :
          if sum(user_hand) > 21 :
            random.choice(cards) == 1
        elif comp_number == 11:
          if sum(comp_hand) > 21:
            random.choice(cards) == 1
        else:
            random.choice(cards) == 11   
        user_hand.append(user_number)
        user_current_score = sum(user_hand)        
        comp_hand.append(comp_number)
        comp_current_score = sum(comp_hand)
        if user_current_score > 21 and comp_current_score > 21 :
          play_again = False
          print(f"Your final hand: {user_hand} and final score: {user_current_score}")
          print(f"Computer`s final hand: {comp_hand} and final score: {comp_current_score}")
          print("You both over 21 no winner!")
        elif user_current_score > 21 :
          play_again = False
          print(f"Your final hand: {user_hand} and final score: {user_current_score}")
          print(f"Computer`s final hand: {comp_hand} and final score: {comp_current_score}")
          print("you are over 21 and lost!")
        elif comp_current_score > 21 :
          play_again = False
          print(f"Your final hand: {user_hand} and final score: {user_current_score}")
          print(f"Computer`s final hand: {comp_hand} and final score: {comp_current_score}")
          print("Computer's hand over 21 and you win!")
        else:
          if comp_current_score > user_current_score:
            print("Computer wins! You lose :( ")         
          else:
            print("you win!")
          