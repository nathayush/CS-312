lst = [1,6,8,4,3,5,4,1,3]

temp = []
for i in range(len(lst), 0, -1):
    temp.append(lst[i-1])

reverse = temp
