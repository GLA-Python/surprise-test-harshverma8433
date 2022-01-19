n = int(input())
a = 1
print(a)
while n>1:
    an = ""
    while a > 0:
        c = a%10
        count = 1
        a //= 10
        while a>0 and a%10==c:
            count += 1
            a //= 10
        an = str(count)+str(c)+an
    print(an)
    a = int(an)
    n -= 1        
    
    
    

        
    




