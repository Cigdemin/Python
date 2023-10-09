# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
for n in student_heights :
  total_height += n
average_height = total_height / len(student_heights)
print(f"total height = {total_height}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(average_height)}")


###Calculating highest score in classroom
highest_score = 0
for score in student_heights:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {score}")