lst = [1,2,3,4,5]

num = sys.maxsize
for i in range(0, len(lst)):
    if lst[i] < num:
        num = lst[i]

min_num = num
