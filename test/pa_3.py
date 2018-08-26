a =[5,6]
b = [7,8,9]
c = a+b

for element in c:
    if c.index(element) == 0:
        numb = element
    else:
        numb+=element

max_numb = numb
