num = 4
lst = [1,6,8,4,3,5,4,1,3]

for i in range(0, len(lst)):
    if lst[i] == num:
        del lst[i]
        break

new_lst = lst
