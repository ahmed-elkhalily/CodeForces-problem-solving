r = 5
i=1
arr = []
while i < r+1:
  c = input().split()
  arr.append(c)
  # working with while
  i += 1
 
for i, row in enumerate(arr):
  for j, col in enumerate(row):
    if (int(col) == 1):
      y = abs(3 - (i+1))
      x = abs(3 - (j+1))
print(x+y)