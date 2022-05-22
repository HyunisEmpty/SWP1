a = input().split()
b = a[0]
c = a[1]
str_b = ""
str_c = ""
for i in range(3):
    str_b += b[2-i]
    str_c += c[2-i]

if int(str_b) > int(str_c):
    print(str_b)
else:
    print(