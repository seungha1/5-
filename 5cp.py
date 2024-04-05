score = input("점수를입력하시오: ")
num_score = int(score)

if num_score >= 71:
  print("A")

elif 70 >= num_score >= 41:
  print("B")

elif 40 >= num_score >= 11:
  print("C")

elif num_score <= 10:
  print("D")
