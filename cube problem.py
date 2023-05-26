def cube(a,b):
    even=[]
    odd=[]
    c=[]
    for i in range(a,b):
        if i%2==0:
            y=i**3
            even.append(y)
        else:
            x=i**3
            odd.append(x)
    
                
    print(even)
    print(odd)
    sum=0
    for i in even:
        sum=sum+i
        a=sum
    print(a)
    for i in odd:
        sum=sum+i
        b=sum
    print(b)
    
    
    c=b-a
    print(c)
    
    
    
   
cube(1,20)
    
    
            
