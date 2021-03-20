name = input()
n = len(name)
arr = []
i = 0
while i < n:
    if not arr.__contains__(name[i]):
        arr.append(name[i])
    i+=1
l = len(arr)
if l % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")