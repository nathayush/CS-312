lst = [1,6,8,4,3,5,4,1,3]

for i in range(1, len(ls)):
    j = i
    while j > 0 and ls[j] < ls[j-1]:
            ls[j], ls[j-1] = ls[j-1], ls[j]
            j -= 1

lst = sort(lst)
