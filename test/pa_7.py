lst = [1,2,3,4,5]

num = 0
for i in range(0, len(lst)):
    if lst[i] > num:
        num = lst[i]

max_num = num
