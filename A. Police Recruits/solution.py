# A. Police Recruits

n =int(input())
ns =input().split()
(i, c, t) = (0,0,0)
while i < n:
    if c == 0 and int(ns[i]) == -1:
        t += 1
    else:
        c+=int(ns[i])
    i+=1
print(t)