a =[5,6]
b = [6,7]
a = a+[1]
a = a+[3]
b = b+[7]
b = b+[8]

if len(a) < len(b):
    a = b
elif len(a) > len(b):
    a = 1
else:
    a = 2

d = a+b
e = d+d
