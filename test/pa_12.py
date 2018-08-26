lst = [1,2,3,4,5,6,7,9,10]
ind = 7
item = 8

temp = lst[ind:]
del lst[ind:]
lst.append(item)
for j in temp:
    lst.append(j)

new_lst = lst
