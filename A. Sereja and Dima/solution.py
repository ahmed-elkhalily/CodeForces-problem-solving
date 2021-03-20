n = int(input())
ns= input().split(" ")
i, s, d = (0, 0, 0)
while i < n:
    if int(ns[0]) < int(ns[len(ns)-1]):
        if i % 2 == 0:
            s+= int(ns[len(ns)-1])
        else :
            d+= int(ns[len(ns)-1])
        ns.remove(ns[len(ns)-1])
    else:
        if i % 2 == 0:
            s+= int(ns[0])
        else:
            d+= int(ns[0])
        ns.remove(ns[0])
    i+=1
print(s,d)