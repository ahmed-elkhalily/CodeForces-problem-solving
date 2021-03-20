ip = input()
upper_case = 0
i=0
while i < len(ip):
    if ord(ip[i]) < 97:
        upper_case += 1
    i+=1
if upper_case > len(ip) / 2: #small
    print(ip.upper())
else:
    print(ip.lower())