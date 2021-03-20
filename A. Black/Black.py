a = input().split(" ")
s = list(input())
t = 0
for el in s:
    t += int(a[int(el) - 1])
print(t)