n = int(input())
ns = input().split()
i = 0
while i < n:
    j = i+1
    while j < n:
        if j-1 < n:
            if int(ns[j]) > int(ns[i]):
                k = ns[j]
                ns[j] = ns[i]
                ns[i] = k
        j+=1
    i+=1
ns_len = len(ns)
result_arr = []
while ns_len  > 0:
    result_arr.append(ns[ns_len-1])
    ns_len -= 1
print(" ".join(result_arr))