print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇
choice1 = input("You are at the cross road. Where do you want to go? Left or Right?").lower()
if choice1 == "left" :
  choice2 = input("Now you came to the lake where there is an island in the middle. Do you want to swim or wait for the boat? Type swim or wait: ").lower()
  if choice2 == "wait" :
    choice3 = input("You reached the island and you have 3 doors infront. Which you will go? Red, Blue or Yellow? :" ).lower()
    if choice3 == "yellow" :
      print("you win! found the treasure.you are looking for a miraculus mirror cause you are tresure for me :) ")
    elif choice3 == "blue" or choice3 == "red":
      print("sorry you were so close to find the treasure(yourself)..Because you are the treasure for me but this is not the end beginning for us :) keep playing games with me !")
    else:
      print("We don`t have a door like that! are you trying to find a bug in game? :)")
  else:
    print("Sorry :( you are drowned! Game over!") 
else:
  print("Game over :( on the right side, there were a hole and you fall")