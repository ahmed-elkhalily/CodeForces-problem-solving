a_b = input().split()
a = int(a_b[0])
b = int(a_b[1])
 
y = 0
while a <= b:
    a *= 3
    b *= 2
    y += 1
print(y)