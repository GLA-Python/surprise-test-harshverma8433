def expanding_list(l):
    l1 = []
    for i in range(0,len(l)-1):
        if l[i+1] - l[i] > 0:
            c = l[i+1] - l[i]
        elif l[i] - l[i+1]>0:
            c = l[i] - l[i+1]
        l1.append(c)

    
    for j in range(0,len(l1)-1):
        if l1[j] < l1[j+1]:
            b = True
        else:
            b = False
            break
    return b

lst = list(map(int,input().split(",")))
print(expanding_list(lst))
