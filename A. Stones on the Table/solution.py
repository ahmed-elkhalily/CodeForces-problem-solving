n =int(input())
ns =list(input())
(i, cnt) = (1,0)
while i < n:
    if ns[i] == ns[i-1]:
        cnt+=1
    i+=1
print(cnt)