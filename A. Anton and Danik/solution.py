#inputs
n = int(input())
s = str(input()).upper()
wins = []
for char in s:
    wins.append(char)
 
# Persons win
A_win= 0
D_win= 0
 
#function
for winner in wins:
  if (winner == "A"):
    A_win +=1
  elif (winner == "D"):
    D_win += 1
if (D_win > A_win):
  print("Danik")
elif (D_win == A_win):
  print("Friendship")
else:
  print("Anton")