#s: success ; t: total; n: i/p no.
n= int(input())
i = 0
t = 0
while i < n:
  x = input().split()
  s = 0
  for el in x:
      s += int(el)
  if s > 1:
    t += 1
  i += 1
print(t)