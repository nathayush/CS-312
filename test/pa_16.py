lst = [1,2,3,4,5]
delimiter = " "

temp = ""
for i in lst:
    temp += str(i)
    temp += str(delimiter)

string = temp[:-1]
