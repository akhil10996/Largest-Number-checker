# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

student_scores = [78, 65, 89, 86, 55, 91, 64, 34]

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(highest_score)

lowest_score = 100
for score in student_scores:
  if score < lowest_score:
    lowest_score = score
print(f"lowest score is: {lowest_score}")
