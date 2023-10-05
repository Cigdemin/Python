print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the roller coaster")
else:
  print("Sorry you have to be taller before you can ride ")
  
#If you want to check the value is equal for some exact number then 
# you have to give == (double equal sign) it means that you just want to check
# if the value input is equal to your request or not. 
# If you just put one = sign then it will give error


#Code Block 2 for calculating modulo: 
# it means that if you devided number with other if the substraction has remainder
# then modulo shows you the number remainder and you use % sign for that)

# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
modulo = number % 2
if modulo == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")