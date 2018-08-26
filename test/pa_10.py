lst = [1,2,3,4,5,6,7,8,9]

start = 3
end = 6

lst2 = []
for i in lst:
    if lst.index(i) >= start and lst.index(i) < end:
        lst2.append(i)
for i in lst2:
    lst.remove(i)

new_lst = lst
