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
#if the number divided by 2 you will see result 0
#if the number is not divided by 2 you will see other number than 0 
if modulo == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#Code block 3 for BMI calculation
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / height ** 2
if BMI <= 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif 18.5 < BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25 <= BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif 30 <= BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")


#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Equal to or over 25 but below 30 they are slightly overweight
#Equal to or over 30 but below 35 they are obese
#Equal to or over 35 they are clinically obese.

