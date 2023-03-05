a=int (100)
b=int (50)
c=int (50)
d=""
if (a>b):
    d="a is greater than b"
    if (b>c):
        print ("b is greater than c"+d)
    elif(c>b):
        print ("c is greater than b"+d)
elif (b>a):
    d="and b is greater than a"
    if (a>c):
        print("a is greater than c"+d)
    elif(c>a):
        print("c is greater than a"+d)
elif (c>a):
    d="and c is greater than a"
    if (b>a):
        print("b is greater than a"+d)
    elif(a>b):
        print("a is greater than b"+d)
elif(a==b):
    d="and a and b are equal"
    if (c>a):
        print("c is greater than a"+d)
    elif(a>c):
        print("a is greater than c"+d)
elif(b==c):
    d="and c and b are equal"
    if (c>a):
        print("c is greater than a"+d)
    elif(a>c):
        print("a is greater than c"+d)
elif(a==c):
    d="and a and c are equal"
    if (c>b):
        print("c is greater than b"+d)
    elif(b>c):
        print("b is greater than c"+d)
else:
    print("something's worng")
    
        
